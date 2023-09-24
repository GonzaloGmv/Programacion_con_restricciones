from ortools.sat.python import cp_model

model = cp_model.CpModel()
solver = cp_model.CpSolver()

numero = model.NewIntVar(0, 99999, 'numero')

# es multiplo de 7 y de 13
model.AddModuloEquality(0, numero, 7)
model.AddModuloEquality(0, numero, 13)

# el primer digito es 5
model.AddDivisionEquality(5, numero, 10000)

# el segundo digito es menor que 6 y mayor que 1
model.Add(numero < 56000)
model.Add(numero > 51000)

# la suma del numero y mi dni es menor que el dni de mi hermano menor pero mayor que el dni de mi primo
# nuestro dni: 03876543
# dni hermano menor: 03930051
# dni primo: 03928595
model.Add(numero+3876543 < 3930146)
model.Add(numero+3876543 > 3928595)

# la raiz del numero es menor que mi codigo postal
# codigo postal: 229
model.Add(numero <= 229*229)

class PrintSolutions(cp_model.CpSolverSolutionCallback):
    """Callback to print every solution."""
    def __init__(self, variable):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variable = variable
    def on_solution_callback(self):
        print(self.Value(self.__variable))

solution_printer = PrintSolutions(numero)
solver.parameters.enumerate_all_solutions = True
status = solver.Solve(model, solution_printer)