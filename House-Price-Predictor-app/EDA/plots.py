"""
This Module is used for Visualization and plots created will be saved in the directory

Developed by Santosh Saxena
on 19/4/2021
"""

# Module Declaration
#---------------------------------#
import os
import sys
import shutil
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
#---------------------------------#

matplotlib.use("Agg")

class Plots:
    def __init__(self,logger , path):
        try:
            """
            Constructor Initialized

            Input : Logger , Path
            Output : N/A

            """
            self.logger = logger
            self.logger.add_in_logs("NAM","Plots")
            self.logger.add_in_logs("BEG","PLots module initialized")
            self.logger.add_in_logs("inf","Data is loading")
            self.path = path
            self.df = pd.read_csv(self.path + "/Input_files/transformed_data.csv")
        except Exception as e:
            self.logger.add_in_logs("ERR" , "plots in initialization")
            self.logger.add_in_logs("LIN" , "Error on line number : {}".format(sys.exc_info()[-1].tb_lineno))
            self.logger.add_in_logs("TYP" , str(e))

    def generating_directory(self):
        try:
            """
            This function will generate the directories to store the plots generated by this module

            Input : N/A
            Output : generation of different directories for plots

            """

            self.logger.add_in_logs("chk","generating directories process initialized")
            self.logger.add_in_logs("inf","creating plots directory for plots")
            if(os.path.isdir(self.path + "/static/plots")):
                shutil.rmtree(self.path + "/static/plots")
            os.mkdir(self.path + "/static/plots")
            self.logger.add_in_logs("chk","Checking previously encoded categorical features")

            self.numeric_categorical = []
            for i in self.df.columns[self.df.dtypes != "object"][self.df[self.df.columns[self.df.dtypes != "object"]].max()  <= 10]:
                if(self.df[i].dtypes == "int"):
                    self.logger.add_in_logs("inf", i + " is previously encoded categorical feature")
                    self.numeric_categorical.append(i)
                else:
                    continue
            self.logger.add_in_logs("pas","Checking previously encoded categorical feature completed")
            self.logger.add_in_logs("pas","generating directories process completed")
    
        except Exception as e:
            self.logger.add_in_logs("ERR" , "plots in generating directories")
            self.logger.add_in_logs("LIN" , "Error on line number : {}".format(sys.exc_info()[-1].tb_lineno))
            self.logger.add_in_logs("TYP" , str(e))
    
    
    def scatter(self):
        try:
            """
            This function is used to create scatter plots and store the plots into the generated libraries

            Input : N/A
            Output : Scatter plots in a directory

            """

            self.logger.add_in_logs("chk","scatter plots process initialized")
            os.mkdir(self.path + "/static/plots/scatter_plot")
            self.logger.add_in_logs("inf","creating scatter_plot directory for scatter plots")
            for i in self.df.columns[self.df.dtypes != "object"]:
                if(i == "SalePrice" or i in self.numeric_categorical):
                    continue
                plt.figure(dpi = 60)
                plt.style.use("classic")
                plt.scatter(self.df[i], self.df["SalePrice"],label=i,s=75)
                plt.xlabel(i)
                plt.ylabel("SalePrice")
                plt.title(i)
                plt.xticks(rotation = 90)
                plt.grid()
                plt.tight_layout(pad = 2)
                plt.legend()
                plt.savefig(self.path + "/static/plots/scatter_plot/"+str(i)+".png")     

            self.logger.add_in_logs("pas","scatter plots process completed")
        except Exception as e:
            self.logger.add_in_logs("ERR" , "plots in scatter plots")
            self.logger.add_in_logs("LIN" , "Error on line number : {}".format(sys.exc_info()[-1].tb_lineno))
            self.logger.add_in_logs("TYP" , str(e))

    def bar_plot(self):
        try:
            """
            This function is used to create the bar plot and store the plots in a directory

            Input : N/A
            Output : bar plots in a particular directory

            """
            self.logger.add_in_logs("chk","bar plot process initialized")
            os.mkdir(self.path + "/static/plots/bar_plot")
            self.logger.add_in_logs("inf","creating bar_plot directory for bar plots")

            for i in self.df.columns[self.df.dtypes == "object"]:
                score = []
                for j in pd.Categorical(self.df[i]).categories:
                    score.append((self.df[i] == j).sum())
                plt.figure(dpi = 60)
                plt.style.use("classic")
                plt.bar(pd.Categorical(self.df[i]).categories , score , label = i)
                plt.xlabel(i)
                plt.ylabel("Number of Observations")
                plt.title(i)
                plt.xticks(rotation = 90)
                plt.grid(True)
                plt.tight_layout(pad = 2)
                plt.legend()
                plt.savefig(self.path + "/static/plots/bar_plot/"+str(i)+".png")

            for i in self.numeric_categorical:
                score = []
                for j in pd.Categorical(self.df[i]).categories:
                    score.append((self.df[i] == j).sum())
                plt.figure(dpi = 60)
                plt.style.use("classic")
                plt.bar(pd.Categorical(self.df[i]).categories , score , label = i)
                plt.xlabel(i)
                plt.ylabel("Number of Observations")
                plt.title(i)
                plt.xticks(rotation = 90)
                plt.grid(True)
                plt.tight_layout(pad = 2)
                plt.legend()
                plt.savefig(self.path + "/static/plots/bar_plot/"+str(i)+".png")

            self.logger.add_in_logs("pas","bar plots process completed")

        except Exception as e:
            self.logger.add_in_logs("ERR" , "plots in bar plots")
            self.logger.add_in_logs("LIN" , "Error on line number : {}".format(sys.exc_info()[-1].tb_lineno))
            self.logger.add_in_logs("TYP" , str(e))
    
    def pie_plots(self):
        try:
            """
            This function will generate pie plots and store the plots in a particular direcoty

            Input : N/A
            Output : Pie Plots in a particular directory

            """
            self.logger.add_in_logs("chk","pie plots process initialized")
            self.logger.add_in_logs("inf","creating a pie plot directory for pie plots")
            os.mkdir(self.path + "/static/plots/pie_plot")

            for i in self.df.columns[self.df.dtypes == "object"]:
                score = []
                for j in pd.Categorical(self.df[i]).categories:
                    score.append((self.df[i] == j).sum())
                plt.figure(dpi = 60)
                plt.pie(score, labels=pd.Categorical(self.df[i]).categories , autopct='%1.2f%%')
                plt.xlabel(i)
                plt.title(i)
                plt.tight_layout(pad = 4)
                plt.savefig(self.path + "/static/plots/pie_plot/"+str(i)+".png")

            for i in self.numeric_categorical:
                score = []
                for j in pd.Categorical(self.df[i]).categories:
                    score.append((self.df[i] == j).sum())
                plt.figure(dpi = 60)
                plt.style.use("classic")
                plt.pie(score, labels=pd.Categorical(self.df[i]).categories , autopct='%1.2f%%')
                plt.xlabel(i)
                plt.title(i)
                plt.tight_layout(pad = 4)
                plt.savefig(self.path + "/static/plots/pie_plot/"+str(i)+".png")
            
            self.logger.add_in_logs("pas","pie plots process complted")

        except Exception as e:
            self.logger.add_in_logs("ERR" , "plots in pie plots")
            self.logger.add_in_logs("LIN" , "Error on line number : {}".format(sys.exc_info()[-1].tb_lineno))
            self.logger.add_in_logs("TYP" , str(e))
    
    def dist_plot(self):
        try:
            """
            This function will generate various distribution plots which will be stored in a particular directory

            Input : N/A
            Output : Distribution plots will be available in a directory 

            """
            self.logger.add_in_logs("chk","dist plot process initialized")
            self.logger.add_in_logs("inf","creating a distribution plot directory for dist plot")

            os.mkdir(self.path + "/static/plots/distribution_plot")

            for i in self.df.columns[self.df.dtypes != "object"]:
                if(i == "SalePrice" or i in self.numeric_categorical):
                    continue
                plt.figure(dpi = 60)
                plt.style.use("classic")
                sns.distplot(self.df[i], label= i)
                plt.xlabel(i)
                plt.ylabel("SalePrice")
                plt.title(i)
                plt.xticks(rotation = 90)
                plt.grid(True)
                plt.tight_layout(pad = 2)
                plt.legend()
                plt.savefig(self.path + "/static/plots/distribution_plot/"+str(i)+".png")

            self.logger.add_in_logs("pas","dist plots process completed")
        except Exception as e:
            self.logger.add_in_logs("ERR" , "plots in dist plot")
            self.logger.add_in_logs("LIN" , "Error on line number : {}".format(sys.exc_info()[-1].tb_lineno))
            self.logger.add_in_logs("TYP" , str(e))


    def box_plot(self):
        try:
            """
            This function will generate box plot and store the plots in a particular directory

            Input : N/A
            Output : Box plots will be available in a particular directory :

            """
            self.logger.add_in_logs("chk","box plot process initialized")
            self.logger.add_in_logs("inf","creating a box plot directory for box plot")

            os.mkdir(self.path + "/static/plots/box_plot")

            for i in self.df.columns[self.df.dtypes != "object"]:
                if(i == "SalePrice" or i in self.numeric_categorical):
                    continue
                plt.figure(dpi = 60)
                plt.style.use("classic")
                plt.boxplot(self.df[i],notch = True)
                plt.xlabel(i)
                plt.title(i)
                plt.xticks(rotation = 90)
                plt.grid(True)
                plt.tight_layout(pad = 2)
                plt.savefig(self.path + "/static/plots/box_plot/"+str(i)+".png")
            self.logger.add_in_logs("pas","box plot initialized")

            self.logger.add_in_logs("pas","Plots process completed")

        except Exception as e:
            self.logger.add_in_logs("ERR" , "eplots in box plots")
            self.logger.add_in_logs("LIN" , "Error on line number : {}".format(sys.exc_info()[-1].tb_lineno))
            self.logger.add_in_logs("TYP" , str(e))

    def plots_package(self):
        try:
            """
            This function integrates all the above functions accordingly and form pieline for the module

            Input : N/A
            Output : N/A

            """
            self.generating_directory()
            self.scatter()
            self.bar_plot()
            self.pie_plots()
            self.dist_plot()
            self.box_plot()
            self.logger.add_in_logs("end","plots module completed")
        except Exception as e:
            self.logger.add_in_logs("ERR" , "plots in package")
            self.logger.add_in_logs("LIN" , "Error on line number : {}".format(sys.exc_info()[-1].tb_lineno))
            self.logger.add_in_logs("TYP" , str(e))



