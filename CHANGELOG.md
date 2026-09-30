# TOML config changelog

toml format changes, newest-first.

### 2026-09-18 — Jagged over WHIR
- `[[circuits]]` sections with `protocol_family = "JAGGED"` accept `dense_pcs = "whir"`; the dense PCS under the jagged reduction was previously always FRI. `dense_pcs` defaults to `"fri"`, so existing configs are unchanged. A WHIR dense section takes the usual WHIR keys (`log_inv_rate`, `num_iterations`, `folding_factors`, `log_degree`, `constraint_degree`, `num_queries`, `grinding_bits_*`, `num_ood_samples`) with the batch size read from `dense_batch`.
- optional `whir_log_inv_rates`: the explicit per-round rate schedule, for implementations that re-commit each round at their own rate instead of WHIR's `mu_{i+1} = mu_i + (k_i - 1)` recurrence. Unset keeps the recurrence.
- a WHIR dense section rejects `multilinear_batching = true`: WHIR batches with the powers of one challenge (`power_batching = true`) or with independent coefficients, and the key would otherwise be read as accepted while modelling neither. Every round of an explicit `whir_log_inv_rates` schedule, and the final domain, is checked against the field's two-adicity, not only round 0.

### 2026-07-23 — SWIRL
- unified SWIRL circuit loading on the OpenVM-style keys; in SWIRL `[[circuits]]` sections: renamed `log_inv_rate` → `log_blowup`, `num_queries` → `whir_num_queries`, `trace_columns` → `num_trace_columns`, `grinding_batching_phase` → `whir_mu_pow_bits`, `swirl_folding_pow_bits` → `whir_folding_pow_bits`
- removed derived SWIRL keys: `num_iterations`, `folding_factors`, `log_degree`, `batch_size`, `power_batching`, `grinding_bits_queries`, `num_ood_samples`, `grinding_bits_ood`, `grinding_bits_folding`, `swirl_whir_k`, `swirl_query_phase_pow_bits`, `air_max_degree`
- moved SWIRL LogUp keys to the `[swirl]` table: `max_interaction_count` → `logup_max_interaction_count`, `log_max_message_length` → `logup_log_max_message_length`, `grinding_bits_lookup` → `logup_pow_bits`
- allow optional circuit-level `proof_size_*` bounds for OpenVM backend-codec proof size estimates; by default proof sizing uses the corresponding `soundness_*` bound where present
- allow optional circuit-level `soundness_*` bounds to be used for security calculations while reporting the unprefixed circuit shape fields as the actual circuit specs
- allow circuit-level `logup_pow_bits` override, falling back to `[swirl].logup_pow_bits`

### 2026-07-23 — Protocol family
- moved `protocol_family` from the `[zkevm]` section to each `[[circuits]]` section, so a VM can mix proof-system families across circuits

### 2026-05-02 — WHIR
- allow custom folding factors in WHIR

### 2026-04-20 (`1d4371a`) — Lookups
- removed `alphabet_size_H`

### 2026-03-16 (`b3f6610`) — FRI
- rename `grinding_bits_batching` → `grinding_batching_phase`
