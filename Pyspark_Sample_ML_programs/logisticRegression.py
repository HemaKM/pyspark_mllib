from pyspark.ml.classification import LogisticRegression
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "samp")
sqlContext = SQLContext(sc)
training = sqlContext.read.format("libsvm").load("D:\Spark\spark-1.6.1-bin-hadoop2.6\data\mllib\sample_libsvm_data.txt")
lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
lrModel = lr.fit(training)
print("Coefficients :" + str(lrModel.coefficients))
print("Intercept :" + str(lrModel.intercept))

"""OUTPUT
Coefficients :(692,[244,263,272,300,301,328,350,351,378,379,405,406,407,428,433,
434,455,456,461,462,483,484,489,490,496,511,512,517,539,540,568],[-7.35398352419
e-05,-9.10273850559e-05,-0.000194674305469,-0.000203006424735,-3.14761833149e-05
,-6.84297760266e-05,1.58836268982e-05,1.40234970914e-05,0.00035432047525,0.00011
4432728982,0.000100167123837,0.00060141093038,0.000284024817912,-0.0001154108473
65,0.000385996886313,0.000635019557424,-0.000115064123846,-0.00015271865865,0.00
0280493380899,0.000607011747119,-0.000200845966325,-0.000142107557929,0.00027390
1034116,0.00027730456245,-9.83802702727e-05,-0.000380852244352,-0.00025315198008
6,0.000277477147708,-0.000244361976392,-0.00153947446876,-0.000230733284113])
Intercept :0.224563159613
"""
