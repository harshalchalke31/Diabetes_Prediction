import numpy as np
import pandas as pd

class DiabetesDataGenerator():
    def __init__(self, means, std_devs):
        self.means = means
        self.std_devs = std_devs

    def generate(self, n_samples):
        data = {
            'Pregnancies': np.random.normal(self.means['Pregnancies'], self.std_devs['Pregnancies'], n_samples),
            'Glucose': np.random.normal(self.means['Glucose'], self.std_devs['Glucose'], n_samples),
            'BloodPressure': np.random.normal(self.means['BloodPressure'], self.std_devs['BloodPressure'], n_samples),
            'SkinThickness': np.random.normal(self.means['SkinThickness'], self.std_devs['SkinThickness'], n_samples),
            'Insulin': np.random.normal(self.means['Insulin'], self.std_devs['Insulin'], n_samples),
            'BMI': np.random.normal(self.means['BMI'], self.std_devs['BMI'], n_samples),
            'DiabetesPedigreeFunction': np.random.normal(self.means['DiabetesPedigreeFunction'], self.std_devs['DiabetesPedigreeFunction'], n_samples),
            'Age': np.random.normal(self.means['Age'], self.std_devs['Age'], n_samples),
        }
        df = pd.DataFrame(data)

        # Ensure that the 'Pregnancies' and 'Outcome' columns are of type int, as they represent count data
        df['Pregnancies'] = df['Pregnancies'].round().astype(int)

        # Clip the values to ensure they fall within a logical range (for example, non-negative)
        df['Pregnancies'] = df['Pregnancies'].clip(lower=0)
        df['Glucose'] = df['Glucose'].clip(lower=0)
        df['BloodPressure'] = df['BloodPressure'].clip(lower=0)
        df['SkinThickness'] = df['SkinThickness'].clip(lower=0)
        df['Insulin'] = df['Insulin'].clip(lower=0)
        df['BMI'] = df['BMI'].clip(lower=0)

        return df