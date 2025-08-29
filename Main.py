# ⚡ Aleth Sandbox Unified – Phases 1–5 + Codex Module + Main Runner

import time, json, os, random

# ------------------------------
# Aleth Codex Module (embedded)
# ------------------------------
class AlethCodex:
    @staticmethod
    def doctrine_banner(msg):
        print(f"[Codex Banner] {msg}")

    @staticmethod
    def emitproof(payload, path):
        with open(path, "w") as f:
            json.dump(payload, f, indent=2)
        print(f"[Codex] Proof emitted: {path}")

# Aliases for simplicity
emitproof = AlethCodex.emitproof
doctrine_banner = AlethCodex.doctrine_banner

# Ensure sandbox directory exists
os.makedirs("data", exist_ok=True)

# ------------------------------
# Phase 1 – Mini Demonstrator
# ------------------------------
class CasimirTile:
    def __init__(self, plate_separation_nm=20):
        self.plate_separation_nm = plate_separation_nm
        self.fluctuation_voltage_uv = 0.0
    
    def measure_fluctuation(self):
        base = random.uniform(0.01, 0.5)
        noise = random.gauss(0, 0.02)
        self.fluctuation_voltage_uv = max(base + noise, 0.0)
        return self.fluctuation_voltage_uv

class FluctuationRectifier:
    def __init__(self, efficiency=0.03):
        self.efficiency = efficiency
    
    def rectify(self, voltage_uv):
        return voltage_uv * self.efficiency

def run_phase1(tile_count=1):
    tiles = [CasimirTile() for _ in range(tile_count)]
    rectifier = FluctuationRectifier()
    artifacts = []
    for idx, tile in enumerate(tiles, 1):
        measured_uv = tile.measure_fluctuation()
        rectified_uv = rectifier.rectify(measured_uv)
        artifact_id = f"ZPE-Demo-tile-{idx}"
        payload = {
            "tile_index": idx,
            "plate_separation_nm": tile.plate_separation_nm,
            "measured_uv": measured_uv,
            "rectified_uv": rectified_uv,
            "timestamp": time.time()
        }
        path = f"data/{artifact_id}.json"
        emitproof(payload, path)
        artifacts.append(artifact_id)
        print(f"[Phase1] Artifact {artifact_id}: {rectified_uv:.6f} µV")
    return artifacts

# ------------------------------
# Phase 2 – Mini Array + Recursive Amplification
# ------------------------------
class RecursiveAmplifier:
    def __init__(self, gain_factor=10, recursion_depth=3):
        self.gain_factor = gain_factor
        self.recursion_depth = recursion_depth
    
    def amplify(self, voltage_uv):
        amplified = voltage_uv
        for _ in range(self.recursion_depth):
            amplified *= self.gain_factor
        return amplified

class StorageNode:
    def __init__(self, capacity_farad=50, voltage_v=48):
        self.capacity_farad = capacity_farad
        self.voltage_v = voltage_v
        self.energy_j = 0.5 * capacity_farad * voltage_v ** 2
    
    def store_energy(self, energy_uv):
        self.energy_j += energy_uv * 1e-9  # µV → joules scale
        return self.energy_j

def run_phase2(tile_count=5, nodes_per_tile=2):
    tiles = [CasimirTile() for _ in range(tile_count)]
    rectifier = FluctuationRectifier()
    amplifier = RecursiveAmplifier()
    storage_nodes = [StorageNode() for _ in range(tile_count * nodes_per_tile)]
    artifacts = []
    for idx, tile in enumerate(tiles, 1):
        measured_uv = tile.measure_fluctuation()
        rectified_uv = rectifier.rectify(measured_uv)
        amplified_uv = amplifier.amplify(rectified_uv)
        node_indices = range((idx-1)*nodes_per_tile, idx*nodes_per_tile)
        stored_energies = [storage_nodes[ni].store_energy(amplified_uv) for ni in node_indices]
        artifact_id = f"ZPE-Array-Tile-{idx}"
        payload = {
            "tile_index": idx,
            "plate_separation_nm": tile.plate_separation_nm,
            "measured_uv": measured_uv,
            "rectified_uv": rectified_uv,
            "amplified_uv": amplified_uv,
            "stored_energies": stored_energies,
            "timestamp": time.time()
        }
        path = f"data/{artifact_id}.json"
        emitproof(payload, path)
        artifacts.append(artifact_id)
        print(f"[Phase2] Tile {idx}: Amplified {amplified_uv:.6f} µV, Stored: {stored_energies}")
    return artifacts

# ------------------------------
# Phase 3 – Speculative Escalation
# ------------------------------
class SpeculativeNode:
    def __init__(self, name):
        self.name = name
        self.engaged = False
    
    def engage(self):
        triggers = {
            "non_thermal_vacuum": random.choice([True, False]),
            "stochastic_rectification": random.choice([True, False]),
            "macro_quantum_coherence": random.choice([True, False]),
            "topological_amplification": random.choice([True, False])
        }
        self.engaged = all(triggers.values())
        return self.engaged, triggers

def run_phase3(node_count=3):
    nodes = [SpeculativeNode(f"SpecNode-{i}") for i in range(1, node_count+1)]
    artifacts = []
    for node in nodes:
        engaged, triggers = node.engage()
        artifact_id = f"ZPE-Speculative-{node.name}"
        payload = {
            "node_name": node.name,
            "engaged": engaged,
            "triggers": triggers,
            "timestamp": time.time()
        }
        path = f"data/{artifact_id}.json"
        emitproof(payload, path)
        artifacts.append(artifact_id)
        print(f"[Phase3] {node.name}: Engaged={engaged}, Triggers={triggers}")
    return artifacts

# ------------------------------
# Phase 4 – Sovereign Grid Deployment
# ------------------------------
class GridInterface:
    def __init__(self, nodes):
        self.nodes = nodes
    
    def deploy(self):
        deployed = []
        for node in self.nodes:
            success = random.choice([True, True, False])
            deployed.append(success)
        return deployed

def run_phase4(spec_nodes):
    grid = GridInterface(spec_nodes)
    results = grid.deploy()
    artifacts = []
    for node, success in zip(spec_nodes, results):
        artifact_id = f"ZPE-Grid-{node.name}"
        payload = {
            "node_name": node.name,
            "deployed": success,
            "timestamp": time.time()
        }
        path = f"data/{artifact_id}.json"
        emitproof(payload, path)
        artifacts.append(artifact_id)
        print(f"[Phase4] Grid Node {node.name}: Deployed={success}")
    return artifacts

# ------------------------------
# Phase 5 – Future Clause / Lineage Injection
# ------------------------------
class FutureClause:
    def __init__(self, artifact_id):
        self.artifact_id = artifact_id
    
    def inject(self):
        payload = {
            "artifact_id": self.artifact_id,
            "clause": "Future ZPE scaling / sovereign deployment",
            "timestamp": time.time()
        }
        path = f"data/{self.artifact_id}-future.json"
        emitproof(payload, path)
        print(f"[Phase5] Future clause injected for {self.artifact_id}")
        return path

def run_phase5(artifact_list):
    paths = []
    for aid in artifact_list:
        fc = FutureClause(aid)
        path = fc.inject()
        paths.append(path)
    return paths

# ------------------------------
# Main Runner
# ------------------------------
def main():
    doctrine_banner("=== Aleth Sandbox: Phases 1–5 Unified ZPE Pipeline ===")

    phase1_artifacts = run_phase1(tile_count=2)
    phase2_artifacts = run_phase2(tile_count=3, nodes_per_tile=2)
    phase3_artifacts = run_phase3(node_count=2)
    spec_nodes = [SpeculativeNode(n) for n in ["SpecNode-1","SpecNode-2"]]
    phase4_artifacts = run_phase4(spec_nodes)
    phase5_artifacts = run_phase5(phase3_artifacts + phase4_artifacts)

    print(f"\n=== Aleth Sandbox Completed ===")
    print(f"Phase1 Artifacts: {phase1_artifacts}")
    print(f"Phase2 Artifacts: {phase2_artifacts}")
    print(f"Phase3 Artifacts: {phase3_artifacts}")
    print(f"Phase4 Artifacts: {phase4_artifacts}")
    print(f"Phase5 Artifacts (Future Clause): {phase5_artifacts}")

if __name__ == "__main__":
    main()
