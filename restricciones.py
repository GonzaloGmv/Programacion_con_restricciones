from ortools.sat.python import cp_model

model = cp_model.CpModel()
solver = cp_model.CpSolver()

numero = model.NewIntVar(0, 99999, 'numero')


# es multiplo de 7 y de 13
model.AddModuloEquality(0, numero, 7)
model.AddModuloEquality(0, numero, 13)

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