import sys
sys.path.append('ClockworkPathfinder/testing/combat_sim')
from run_grind_comprehensive import run_suite_tier

print("=" * 110)
print("TESTING 50% BODYGUARD REDIRECTION FOR SCHOLAR & CHIRURGEON")
print("400 Trials per condition in The Neither and High Radiant")
print("=" * 110)

environments = ["the_neither", "high_radiant"]
for env in environments:
    print(f"\n######################################################################")
    print(f"ENVIRONMENT: {env.upper()}")
    print(f"######################################################################")
    for elvl in [3, 4]:
        for heal in [0.0, 0.50]:
            res = run_suite_tier(enemy_level=elvl, heal_pct=heal, num_runs=400, env=env)
            print("-" * 100)
            print(f"Enemies: Lv {elvl} | Heal: {heal*100:.0f}% | Avg Waves: {res['avg_waves']:.2f} | Max Waves: {res['max_waves']}")
            print(f"{'Rank':<5} | {'Class':<20} | {'Lifespan':<16} | {'Wave 1 Surv %':<16} | {'Avg Rounds'}")
            print("-" * 100)
            for r, (c, df, w1, rf) in enumerate(res['classes'], 1):
                print(f"#{r:<4} | {c:<20} | Fight #{df:4.2f}    | {w1:5.1f}%          | {rf:4.1f} rounds")

