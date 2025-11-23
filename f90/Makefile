FC     = gfortran
FFLAGS = -fopenmp -g -fcheck=all
LIBS   = -L../../LIB/ispack-3.2.2 -lispack3
TARGET1 = main
TARGET2 = conv

all: ${TARGET1} ${TARGET2} clean
${TARGET1}: ${TARGET1}.o
	${FC} ${TARGET1}.o ${FFLAGS} ${LIBS} -o ${TARGET1}
${TARGET2}: ${TARGET2}.o
	${FC} ${TARGET2}.o ${FFLAGS} ${LIBS} -o ${TARGET2}
${TARGET1}.o: ${TARGET1}.f90
	${FC} ${TARGET1}.f90 ${FFLAGS} ${LIBS} -c
${TARGET2}.o: ${TARGET2}.f90
	${FC} ${TARGET2}.f90 ${FFLAGS} ${LIBS} -c
clean:; rm -f ./*.o 
veryclean:; rm -f ./*.o *.mod ${TARGET1} ${TARGET2}
