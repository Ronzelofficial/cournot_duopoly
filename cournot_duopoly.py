from sympy import *
x, y, z, t, q, Q = symbols('x y z t q Q')

def simultaneous_duopoly(demand, cost1, cost2):
        main1 = demand*x - cost1
        profit1 = simplify(main1)
        deriv1 = diff(profit1, x)

        main2 = demand*y - cost2
        profit2 = simplify(main2)
        deriv2 = diff(profit2, y)

        cv = solve((deriv1, deriv2), (x, y))

        firstsub1 = profit1.subs(x, cv[x])
        firm1_profit = firstsub1.subs(y, cv[y])
        firstsub2 = profit2.subs(y, cv[y])
        firm2_profit = firstsub2.subs(x, cv[x])
        price1 = demand.subs(x, cv[x])
        price2 = price1.subs(y, cv[y])

        print("the market clearing quantity for the simultaneous move game is", cv[x], "for firm1 and", cv[y], "for firm2")
        print("the firms compete by quantity and therefore set the same price", price2)
        print("firm1's simultaneous move profit is", firm1_profit)
        print("firm2's simultaneous move profit is", firm2_profit)


def sequential_duopoly(demand, cost1, cost2):
        main1 = demand * x - cost1
        profit1 = simplify(main1)

        main2 = demand * y - cost2
        profit2 = simplify(main2)
        deriv2 = diff(profit2, y)

        br2 = solve(deriv2, y)

        expr2 = profit1.subs(y, br2[0])
        foc = diff(expr2, x)
        firm1quan = solve(foc, x)
        firm2quan = br2[0].subs(x, firm1quan[0])

        firstsub1 = profit1.subs(x, firm1quan[0])
        firm1_profit = firstsub1.subs(y, firm2quan)
        firstsub2 = profit2.subs(y, firm2quan)
        firm2_profit = firstsub2.subs(x, firm1quan[0])

        print("firm1's optimal quantity playing 1st in the sequential move game is", firm1quan[0])
        print("firm2's optimal quantity playing 2nd in the sequential move game is", firm2quan)
        print("firm1's profit in the sequential move game playing 1st is", firm1_profit)
        print("firm2's profit in the sequential move game playing 2nd is", firm2_profit)

def symmetric_cartel(demand, cost1, cost2):
        main = demand*x + demand*y - cost1 - cost2
        profit = simplify(main)
        deriv1 = diff(profit, x)
        deriv2 = diff(profit, y)
        cv = solve((deriv1, deriv2), (x, y))
        print("firm1 colludes and produces", cv[x])
        print("firm2 colludes and produces", cv[y])
        if cv[x] == cv[y]:
            profitx = profit.subs(x, cv[x])
            profity = profitx.subs(y, cv[y])
            firmprofit = profity/2
            print("the profit an individual firm makes under cooperation is", firmprofit)
        else:
            print("aysemtric cartel")

def folk_theorem(demand, cost1, cost2):
    main1sim = demand * x - cost1
    profit1sim = simplify(main1sim)
    deriv1sim = diff(profit1sim, x)

    main2sim = demand * y - cost2
    profit2sim = simplify(main2sim)
    deriv2sim = diff(profit2sim, y)

    cvsim = solve((deriv1sim, deriv2sim), (x, y))

    firstsub1sim = profit1sim.subs(x, cvsim[x])
    firm1_profitsim = firstsub1sim.subs(y, cvsim[y])
    firstsub2sim = profit2sim.subs(y, cvsim[y])
    firm2_profitsim = firstsub2sim.subs(x, cvsim[x])

    main = demand * x + demand * y - cost1 - cost2
    profit = simplify(main)
    deriv1 = diff(profit, x)
    deriv2 = diff(profit, y)
    cv = solve((deriv1, deriv2), (x, y))
    if cv[x] == cv[y]:
        profitx = profit.subs(x, cv[x])
        profity = profitx.subs(y, cv[y])
        firmprofit = profity / 2

        main2 = demand * y - cost2
        profit2 = simplify(main2)
        deriv2 = diff(profit2, y)

        br2 = solve(deriv2, y)
        deviation = br2[0].subs(x, cv[x])

        devprofity = profit2.subs(y, deviation)
        devprofitx = devprofity.subs(x, cv[x])

        folk = (devprofitx - firmprofit) / (devprofitx - firm1_profitsim)

        print("the profit an individual firm makes under cooperation is", firmprofit, "every period they collude")
        print("if a firm deviates from the cartel they can make ", devprofitx, "in a single period, the cartel would then break down and each firm will only earn", firm1_profitsim, "each period")
        print("the folk theorem suggests that both firms can maintain cullusion if they discount the future at the rate of at least", folk)
    else:
        print("we cannot work with an aysemtric cartel, yet!!!!")

simultaneous_duopoly(100-x-y, 1/2*x**2, 1/2*y**2)
sequential_duopoly(100-x-y, 1/2*x**2, 1/2*y**2)
symmetric_cartel(100-x-y, 1/2*x**2, 1/2*y**2)
folk_theorem(100-x-y, 1/2*x**2, 1/2*y**2)
