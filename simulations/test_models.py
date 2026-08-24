from __future__ import annotations

from pathlib import Path

import mujoco


SIM_ROOT = Path(__file__).resolve().parent


def compile_and_step(relative_path: str, steps: int = 100) -> tuple[int, int, int]:
    model = mujoco.MjModel.from_xml_path(str(SIM_ROOT / relative_path))
    data = mujoco.MjData(model)
    for _ in range(steps):
        mujoco.mj_step(model, data)
    return model.nbody, model.nq, model.nu


def main() -> None:
    results = {
        "retail": compile_and_step("retail_humanoids/retail.xml"),
        "security": compile_and_step("quadruped_security/security.xml"),
        "openquad": compile_and_step("open_quadruped_raas/open_quadruped.xml"),
        "restroom": compile_and_step("restroom_cleaning/restroom.xml"),
        "warehouse": compile_and_step("warehouse_capability/warehouse.xml"),
    }
    assert results["retail"][0] >= 5
    assert results["security"][0] >= 4
    assert results["openquad"][0] >= 4
    assert results["restroom"][0] >= 5
    assert results["warehouse"][0] >= 7
    print("MuJoCo model smoke tests passed:", results)


if __name__ == "__main__":
    main()
