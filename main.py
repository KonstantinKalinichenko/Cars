import calculator


if __name__ == '__main__':
    calc = calculator.Calculator(years = 10)
    calc.add_car(
        calculator.Car("Toyota Corolla", 40000, 7, 1200, 2500),
    )
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3", 200001, 5500, 150),
    )

    calc.print_cars()
