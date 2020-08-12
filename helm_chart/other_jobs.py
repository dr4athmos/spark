data = {
    'code': textwrap.dedent("""
        import org.apache.spark.mllib.clustering.{KMeans, KMeansModel}
        import org.apache.spark.mllib.linalg.Vectors

        // Load and parse the data
        //val data = sc.textFile("kmeans_data.txt")
        //val parsedData = data.map(s => Vectors.dense(s.split(' ').map(_.toDouble))).cache()

        val data = Array(1, 2, 3, 4, 5)
        val distData = sc.parallelize(data)
        
        // Cluster the data into two classes using KMeans
        val numClusters = 2
        val numIterations = 20
        val clusters = KMeans.train(distData, numClusters, numIterations)

        // Evaluate clustering by computing Within Set Sum of Squared Errors
        val WSSSE = clusters.computeCost(parsedData)
        println(s"Within Set Sum of Squared Errors = $WSSSE")

        // Save and load model
        //clusters.save(sc, "target/org/apache/spark/KMeansExample/KMeansModel")
        //val sameModel = KMeansModel.load(sc, "target/org/apache/spark/KMeansExample/KMeansModel")
        """)
    }

data = {
    'code': textwrap.dedent("""
        sc.addPyFile("dependencies.zip")
        import numpy
        """)
    }

    
    