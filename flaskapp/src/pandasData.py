import pandas as pd
class PandasData():
    def __init__(self,name_run) -> None:
        self.name_run = name_run
        self.df = pd.DataFrame(columns=['data','temperatura','umidade'])
    
    def add_line(self, data: str, temperatura: float, umidade: float):
        self.df.loc[len(self.df)] = [data, temperatura, umidade]
        if len(self.df)%100 == 0:
            self.save_data()

    def save_data(self):
        self.df.to_csv(f"{self.name_run}.csv",index=False)