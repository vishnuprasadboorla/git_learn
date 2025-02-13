import com.github.music.of.the.ainur.almaren.builder.Core.Implicit 
import com.github.music.of.the.ainur.almaren.Almaren
 
 
val almaren = Almaren("Demo1")
val spark = almaren.spark.getOrCreate()
 
val df_res = almaren.builder
.sourceJdbc("jdbc:postgresql://w3.training5.modak.com:5432/postgres","org.postgresql.Driver","select * from sample_table_mt24066",Some("mt24066"),Some("mt24066@m10y24"))
.targetJdbc("jdbc:postgresql://w3.training5.modak.com:5432/training","org.postgresql.Driver","mt24066_nabu2",SaveMode.Overwrite,Some("mt24066"),Some("mt24066@m10y24"))
