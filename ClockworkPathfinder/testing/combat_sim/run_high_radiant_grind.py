import sys
sys.path.append('ClockworkPathfinder/testing/combat_sim')
from run_grind_comprehensive import run_suite_tier

print("=" * 110)
print("RUNNING HIGH RADIANT / HIGH POWER ZONE: 4 PCs (Lv 5) vs Consecutive Waves of Lv 3 and Lv 4 Enemies")
print("Active Features: Inductive Arc Projectors, Scholar +2 Hit Telemetry & 15 Temp HP Barrier Pulses")
print("400 Trials per condition (2,400 Gauntlets Total in High Radiant)")
print("=" * 110)

suites = [
    (3, 0.0),
    (3, 0.10),
    (3, 0.50),
    (4, 0.0),
    (4, 0.10),
    (4, 0.50),
]

for elvl, heal in suites:
    res = run_suite_tier(enemy_level=elvl, heal_pct=heal, num_runs=400, env="high_radiant")
    print("\n" + "=" * 110)
    print(f"ENEMIES: LEVEL {res['enemy_level']} | BETWEEN-FIGHT HEALING: {res['heal_pct']*100:.0f}% [HIGH RADIANT]")
    print(f"Squad Performance: Avg Waves Won: {res['avg_waves']:.2f} | Avg Rounds: {res['avg_rounds']:.1f} | Max Waves Cleared: {res['max_waves']}")
    print("-" * 110)
    print(f"{'Rank':<5} | {'Class / Archetype':<22} | {'Lifespan (Avg Death Fight #)':<30} | {'Survive Wave 1 %':<18} | {'Avg Rounds Fought'}")
    print("-" * 110)
    for rank, (disp, avg_df, surv_w1, avg_rf) in enumerate(res['classes'], 1):
        print(f"#{rank:<4} | {disp:<22} | Fight #{avg_df:4.2f}                       | {surv_w1:5.1f}%             | {avg_rf:4.1f} rounds")

