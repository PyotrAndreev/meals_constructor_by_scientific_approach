class Elements:
    def __int__(self):
        self.carbs =  4  # per gram
        self.proteins = 9  # gram
        self.fats = 4  # gram

    def calcul_kcal(self):  # here gram quantity
        pass


class Person:
    def __int__(self, weight: float, height: float, age: float, sex: bool, pal: float,
                aim_weight: float = None, lean_weight: float = None):
        self.weight = weight  # in kg
        self.aim_weight = aim_weight if aim_weight else weight  # in kg
        self.lean_weight = lean_weight  # in kg
        self.height = height  # in sm
        self.age = age  # in age
        self.sex = sex
        self.pal = pal  # Physical Activity Level

        # Basal Metabolic Rate
        if sex:  # man, 1
            self.bmr =
        elif not sex:  # woman, 0
            self.bmr =
        else:
            raise ValueError(f'sex must belong the set(0, 1), where 0 - woman, 1 - man. In your case sex = {sex}')

        self.tdee = self.bmr * pal  # Total Daily Energy Expenditure


class Product:
    def __init__(self, kcal: float, carbs: float, proteins: float, fats: float, compatible_with: set):
        self.kcal = kcal
        self.carbs = carbs
        self.proteins = proteins
        self.fats = fats


class Meal:
    def __init__(self, ):
        pass


class MealDay:
    def __init__(self, n_meals: int, carbs_decreasing: bool|list, ):
        pass



