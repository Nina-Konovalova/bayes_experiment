from GPyOptimization import BayesianOptimization
import numpy as np
import pandas as pd
from Configurations.arguments import parse_args


def optimization(args):
    x_e = pd.read_csv(args.path_experiments)
    x_e = np.array(x_e)
    x_parameter_pol = np.array(pd.read_csv('data/parameters/X_train_gauss_20.csv'))
    print('shape', x_parameter_pol.shape)

    for i in range(len(x_e)):
        gp_model = BayesianOptimization(args.model_type, x_e[i], i, args.kernel_type)
        gp_model.optimization_step(x_parameter_pol, args.number_steps,
                                   args.path_for_save, args.acquisition_type)


def main():
    args = parse_args()
    optimization(args)


if __name__ == '__main__':
    main()
