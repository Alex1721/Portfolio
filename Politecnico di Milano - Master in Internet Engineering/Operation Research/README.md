# biogas-plant-mixed-integer-linear-program

Operation research to find the perfect location of biogas plants in order to maximize the incomes generated by those plants. I'm using the python mip library in order to solve this problem. Use Jupyter notebook.

## Biogas plants location

An association of $n$ farmers wants to open $p$ plants to produce energy from biogas.
Each plant will be opened at a farm of a member of the association and will be powered with corn chopping purchased from the farm itself or from other neighboring farms.

Each farm $i$ can provide at most $c_i$ tons of corn chopping, with a percentage of dry matter $a_i$. As you may know, dry matter is the key component of corn chopping used for biogas production. In order to maintain the quality of produced energy, each plant must burn a mixture of corn chopping with a percentage of dry matter between $k_{min}$ and $k_{max}$.

At most one plant can be located in each farm, and every farm can sell its corn chopping to one and only one plant.

Each farm $i$ is located at coordinates $x_i$ and $y_i$, representing respectively its latitude and longitude, and the cost of moving corn chopping from a farm $i$ to a farm $j$ is proportional to the euclidean distance between the two farms (it does not depend on the actual quantity moved, since the trucks used for this transportations are sufficiently big).

Under such conditions, every plant produces $Q$ kWh of energy per ton of corn chopping burned. The energy produced by each plant will be fed into the national electricity system, at a unitary price of $b$ (€/kWh). Moreover, due to state regulations, each plant must not produce more than $M$ kWh of energy.

You must locate $p$ plants among the available farms and assign the farms that will supply each plant, with the goal of maximizing the total revenues of the association.

## Biogas plant

You want to plan the two-year supply of raw materials for a biogas power plant. Such a plant produces energy by burning biogas, which is obtained from the bacterial fermentation of organic wastes.
Specifically, your plant is powered by corn chopping, a residual of agro-industrial operations that you can purchase from 5 local farms.
The table below shows the quarterly capacity of each farm for the next two years. Quantities are measured in tons.

| Farm |  T1  |  T2  |  T3  | T4  |  T5  |  T6  |  T7  | T8  |
| :--- | :--: | :--: | :--: | :-: | :--: | :--: | :--: | :-: |
| 1    | 700  | 1500 | 700  |  0  |  0   | 700  | 1500 |  0  |
| 2    | 1350 |  0   | 450  |  0  | 1350 |  0   | 450  |  0  |
| 3    |  0   | 1500 | 1500 |  0  |  0   | 1500 | 1500 |  0  |
| 4    | 820  | 1560 | 820  |  0  | 820  | 1560 | 820  |  0  |
| 5    |  0   | 680  | 1080 |  0  |  0   | 680  | 1080 |  0  |

Due to crop rotations and corn harvesting periods, farms are unable to supply material in some quarters. Moreover the types of corn chopping provided are different, each coming with its own unitary purchase price, unitary storage cost and percentage of dry matter. The table below shows a summary of these information.

| Farm | Purchase price | Storage cost | Dry matter |
| :--- | :------------: | :----------: | :--------: |
| 1    |      0.20      |    0.002     |     15     |
| 2    |      0.18      |    0.012     |     28     |
| 3    |      0.19      |    0.007     |     35     |
| 4    |      0.21      |    0.011     |     37     |
| 5    |      0.23      |    0.015     |     42     |

Your biogas plant must operate by burning a mixture of corn choppings with a dry matter percentage between 20% and 40%. Under these conditions, the yield is 421.6 kWh of energy per ton of burned material. The energy produced by the plant is sold on the market at a price of 0.28 $/kWh.

Due to state regulations, all biogas plants can produce a maximum of 1950 MWh of energy per quarter. You are allowed to store corn chopping in a silo, whose total capacity is of 500 tons.

Plan the supply and inventory of your biogas plant with the goal of maximizing your profits (i.e., revenues minus costs).