"""A jagged circuit may sit on WHIR instead of FRI (Ziren's inner ring).

The jagged reduction analysis is the same either way; what changes is which
dense PCS carries the committed polynomial, and — for implementations that
re-commit at their own rate — the per-round rate schedule.
"""

from soundcalc.circuits.jagged import JaggedCircuit
from soundcalc.pcs.fri import FRI
from soundcalc.pcs.whir import WHIR, WHIRConfig
from soundcalc.zkvms import sp1, ziren


def test_ziren_core_is_jagged_over_whir():
    vm = ziren.load()
    core = next(c for c in vm.get_circuits() if c.name == "core")
    assert isinstance(core, JaggedCircuit)
    assert isinstance(core.pcs.dense_pcs, WHIR)


def test_sp1_stays_jagged_over_fri():
    """`dense_pcs` defaults to FRI, so configs that omit it are unchanged."""
    vm = sp1.load()
    core = next(c for c in vm.get_circuits() if c.name == "core")
    assert isinstance(core, JaggedCircuit)
    assert isinstance(core.pcs.dense_pcs, FRI)


def _whir_config(**overrides) -> WHIRConfig:
    params = dict(
        hash_size_bits=248,
        log_inv_rate=2,
        num_iterations=3,
        folding_factors=[3, 6, 6],
        field="KoalaBear^4",
        log_degree=21,
        batch_size=32,
        power_batching=False,
        grinding_batching_phase=0,
        constraint_degree=3,
        grinding_bits_folding=[[0, 0, 0], [0] * 6, [0] * 6],
        num_queries=[124, 88, 85],
        grinding_bits_queries=[16, 16, 16],
        num_ood_samples=[2, 2],
        grinding_bits_ood=[0, 0],
    )
    params.update(overrides)
    from soundcalc.common.fields import parse_field

    params["field"] = parse_field(params["field"])
    return WHIRConfig(**params)


def test_whir_rate_schedule_defaults_to_the_recurrence():
    """Unset `log_inv_rates` keeps mu_{i+1} = mu_i + (k_i - 1)."""
    whir = WHIR(_whir_config())
    assert whir.log_inv_rates == [2, 4, 9, 14]


def test_whir_rate_schedule_can_be_given_explicitly():
    """Ziren re-commits round r at 2 + 3(r+1) instead."""
    whir = WHIR(_whir_config(log_inv_rates=[2, 5, 8, 8]))
    assert whir.log_inv_rates == [2, 5, 8, 8]
