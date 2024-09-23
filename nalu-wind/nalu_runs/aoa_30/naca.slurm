#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=96
#SBATCH --time=12:00:00
#SBATCH --account=hfm
#SBATCH --job-name=naca_0021_aoa_30
#SBATCH --switches=1@01:00:00
#SBATCH --qos=high
#SBATCH --mail-user=shreyas.bidadi@nrel.gov
#SBATCH --mail-type=BEGIN,END,FAIL

module purge
export SPACK_MANAGER=/scratch/sbidadi/gbetrie/exawind-manager
source ${SPACK_MANAGER}/start.sh
spack-start
module restore && module swap PrgEnv-cray PrgEnv-intel
quick-activate /scratch/sbidadi/gbetrie/exawind-manager/environments/exawind-kestrel
spack load exawind

ranks_per_node=104
mpi_ranks=$(expr $SLURM_JOB_NUM_NODES \* $ranks_per_node)

export LD_PRELOAD=/nopt/nrel/apps/cray-mpich-stall/libs_mpich_nrel_intel/libmpi_intel.so.12
ldd `which naluX` | grep mpi 

export MPICH_VERSION_DISPLAY=1
export MPICH_OFI_CQ_STALL=1
export MPICH_OFI_CQ_STALL_USECS=16
export MPICH_OFI_CXI_COUNTER_REPORT=2
export MPICH_ENV_DISPLAY=1

export FI_MR_CACHE_MONITOR=memhooks
export MPICH_SMP_SINGLE_COPY_MODE=NONE
export FI_CXI_RX_MATCH_MODE=software

BINDW='--cpu_bind=map_cpu:0,52,13,65,26,78,39,91,1,53,14,66,27,79,40,92,2,54,15,67,28,80,41,93,3,55,16,68,29,81,42,94,4,56,17,69,30,82,43,95,5,57,18,70,31,83,44,96,6,58,19,71,32,84,45,97,7,59,20,72,33,85,46,98,8,60,21,73,34,86,47,99,9,61,22,74,35,87,48,100,10,62,23,75,36,88,49,101,11,63,24,76,37,89,50,102,12,64,25,77,38,90,51,103'

echo "Job name       = $SLURM_JOB_NAME"
echo "Num. nodes     = $SLURM_JOB_NUM_NODES"
echo "Num. MPI Ranks = $mpi_ranks"
echo "Num. threads   = $OMP_NUM_THREADS"
echo "Working dir    = $PWD"

srun -u -N4 -n384 --ntasks-per-node=96 --distribution=block:cyclic $BINDW naluX -i naca0021_aoa30.yaml
