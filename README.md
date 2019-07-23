# README.txt 

01_make_maps_DFILE_VVV_TYID.py   

# 概要:  
  J-OFURO3のデータファイルから台風時の分布図を作成  
  Ferrt, Best_Trackが必要  

# 引数:   
- DFILE: J3のデータファイル(ex. J-OFURO3_LHF_V1.0_MONTHLY_HR_2002.nc)  
- VVV  : 変数名 (ex. LHF)  
- TYID : 台風ID（ex. 1013）  
  
# 出力:   
  台風を中心とする値の分布  
  台風の位置はBestrackに準じ、  
  J3の値はDaily meanから線型内挿で作成される  
  
# 内部コード:   
	make_jnl.csh: ferret実行用スクリプト作成  
        tymap.jnl: 台風時の分布図作成のferretスクリプト  

