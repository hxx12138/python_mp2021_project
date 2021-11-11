emo_data = read.csv('data/emo_data_2.csv', encoding = 'utf-8')
head(emo_data)
label0 = subset(emo_data, label == '0')
label1 = subset(emo_data, label == '1')

(ks_anger = ks.test(label0[['anger']], label1[['anger']]))
(ks_disgust = ks.test(label0[['disgust']], label1[['disgust']]))
(ks_joy = ks.test(label0[['joy']], label1[['joy']]))
(ks_sadness = ks.test(label0[['sadness']], label1[['sadness']]))
(ks_fear = ks.test(label0[['fear']], label1[['fear']]))

var(label0[['disgust']])
sd(label0[['disgust']])
sd(label1[['disgust']])
mean(label0[['disgust']])
mean(label1[['disgust']])
length(label0[['anger']])
length(label1[['anger']])


# 对所有文本的情绪进行分析
true_false_emo_notext = read.csv('data/true_false_emo_notext.csv')
head(true_false_emo_notext)
t = subset(true_false_emo_notext, label2 == 'TRUE')
f = subset(true_false_emo_notext, label2 == 'FALSE')
l = subset(true_false_emo_notext, label3 == 'L')
h = subset(true_false_emo_notext, label3 == 'H')
lt = subset(true_false_emo_notext, label == 'LT')
ht = subset(true_false_emo_notext, label == 'HT')
lf = subset(true_false_emo_notext, label == 'LF')
hf = subset(true_false_emo_notext, label == 'HF')

# true-false
(ks_anger = ks.test(t[['anger']], f[['anger']]))
(ks_disgust = ks.test(t[['disgust']], f[['disgust']]))
(ks_joy = ks.test(t[['joy']], f[['joy']]))
(ks_sadness = ks.test(t[['sadness']], f[['sadness']]))
(ks_fear = ks.test(t[['fear']], f[['fear']]))

# lt-ht
(ks_anger = ks.test(lt[['anger']], ht[['anger']]))
(ks_disgust = ks.test(lt[['disgust']], ht[['disgust']]))
(ks_joy = ks.test(lt[['joy']], ht[['joy']]))
(ks_sadness = ks.test(lt[['sadness']], ht[['sadness']]))
(ks_fear = ks.test(lt[['fear']], ht[['fear']]))

# lf-hf
(ks_anger = ks.test(lf[['anger']], hf[['anger']]))
(ks_disgust = ks.test(lf[['disgust']], hf[['disgust']]))
(ks_joy = ks.test(lf[['joy']], hf[['joy']]))
(ks_sadness = ks.test(lf[['sadness']], hf[['sadness']]))
(ks_fear = ks.test(lf[['fear']], hf[['fear']]))

# l-h
(ks_anger = ks.test(l[['anger']], h[['anger']]))
(ks_disgust = ks.test(l[['disgust']], h[['disgust']]))
(ks_joy = ks.test(l[['joy']], h[['joy']]))
(ks_sadness = ks.test(l[['sadness']], h[['sadness']]))
(ks_fear = ks.test(l[['fear']], h[['fear']]))


# HLT_LHF_emo_KStest
lm_data = read.csv('data/lm_data_6.csv')
head(lm_data)
HLT = subset(lm_data, followers_count>=1000 & label=='LT')
LHF = subset(lm_data, followers_count<1000 & label=='HF')
head(LHF)
(ks_anger = ks.test(HLT[['anger']], LHF[['anger']]))
(ks_disgust = ks.test(HLT[['disgust']], LHF[['disgust']]))
(ks_joy = ks.test(HLT[['joy']], LHF[['joy']]))
(ks_sadness = ks.test(HLT[['sadness']], LHF[['sadness']]))
(ks_fear = ks.test(HLT[['fear']], LHF[['fear']]))


sent_emo_short_text = read.csv('short_text_sentiment_classifier/data/emo_data.csv', encoding = 'utf-8')
head(sent_emo_short_text)
HLT = subset(sent_emo_short_text, label == 'LT' &  followers_count>=1000)
LHF = subset(sent_emo_short_text, label == 'HF' & followers_count<1000)
(ks_anger = ks.test(HLT[['anger']], LHF[['anger']]))
(ks_disgust = ks.test(HLT[['disgust']], LHF[['disgust']]))
(ks_joy = ks.test(HLT[['joy']], LHF[['joy']]))
(ks_sadness = ks.test(HLT[['sadness']], LHF[['sadness']]))
(ks_fear = ks.test(HLT[['fear']], LHF[['fear']]))


emo_df_key_words = read.csv('data/emo_df_key_words.csv', encoding = 'utf-8')
head(emo_df_key_words)
LT = subset(emo_df_key_words, label == 'LT')
HF = subset(emo_df_key_words, label == 'HF')
head(LT)
(ks_anger = ks.test(LT[['angry']], HF[['angry']]))
(ks_disgust = ks.test(LT[['disgusted']], HF[['disgusted']]))
(ks_joy = ks.test(LT[['happy']], HF[['happy']]))
(ks_sadness = ks.test(LT[['sad']], HF[['sad']]))
(ks_fear = ks.test(LT[['scared']], HF[['scared']]))



############################################## KStest-emo-avg ######################################
# HLT_LHF_emo_KStest
avg_data = read.csv('data/classify_data_3_emo_cla_logit.csv')
head(avg_data)
HLT = subset(avg_data, followers_count>=1000 & label=='LT')
LHF = subset(avg_data, followers_count<1000 & label=='HF')
head(LHF)
(ks_anger = ks.test(HLT[['anger_avg']], LHF[['anger_avg']]))
(ks_disgust = ks.test(HLT[['disgust_avg']], LHF[['disgust_avg']]))
(ks_joy = ks.test(HLT[['joy_avg']], LHF[['joy_avg']]))
(ks_sadness = ks.test(HLT[['sadness_avg']], LHF[['sadness_avg']]))
(ks_fear = ks.test(HLT[['fear_avg']], LHF[['fear_avg']]))

# T-F
KStest <- function(n1, n2){
  print(ks.test(n1[['anger_avg']], n2[['anger_avg']]))
  print(ks.test(n1[['disgust_avg']], n2[['disgust_avg']]))
  print(ks.test(n1[['joy_avg']], n2[['joy_avg']]))
  print(ks.test(n1[['sadness_avg']], n2[['sadness_avg']]))
  print(ks.test(n1[['fear_avg']], n2[['fear_avg']]))
}

T_news = subset(avg_data, false==0)
F_news = subset(avg_data, false==1)
KStest(T_news, F_news)

# L-H
L_news = subset(avg_data, label=='LT' | label=='LF')
H_news = subset(avg_data, label=='HT' | label=='HF')
KStest(L_news, H_news)
###################################################################################################


############################################## KStest-emo-kw ######################################
# HLT_LHF_emo_KStest
kw_data = read.csv('data/classify_data_3_emo_cla_prob_logit.csv')
head(kw_data)
HLT = subset(kw_data, followers_count>=1000 & label=='LT' & emo_prob_kw!=-1)
LHF = subset(kw_data, followers_count<1000 & label=='HF' & emo_prob_kw!=-1)
head(LHF)
KStest <- function(n1, n2){
  print(ks.test(n1[['anger_kw']], n2[['anger_kw']]))
  print(ks.test(n1[['disgust_kw']], n2[['disgust_kw']]))
  print(ks.test(n1[['joy_kw']], n2[['joy_kw']]))
  print(ks.test(n1[['sadness_kw']], n2[['sadness_kw']]))
  print(ks.test(n1[['fear_kw']], n2[['fear_kw']]))
}
KStest(HLT, LHF)

# T-F
T_news = subset(kw_data, false==0 & emo_prob_kw!=-1)
F_news = subset(kw_data, false==1 & emo_prob_kw!=-1)
KStest(T_news, F_news)

# L-H
L_news = subset(kw_data, label=='LT' & emo_prob_kw!=-1 | label=='LF' & emo_prob_kw!=-1)
H_news = subset(kw_data, label=='HT' & emo_prob_kw!=-1 | label=='HF' & emo_prob_kw!=-1)
KStest(L_news, H_news)
###################################################################################################

############################################## KStest-emo-stsc ######################################
# HLT_LHF_emo_KStest
stsc_data = read.csv('data/classify_data_3_emo_cla_prob_logit.csv')
head(stsc_data)
HLT = subset(stsc_data, followers_count>=1000 & label=='LT' & emo_prob_stsc!='-1')
LHF = subset(stsc_data, followers_count<1000 & label=='HF' & emo_prob_stsc!='-1')
head(LHF)
KStest <- function(n1, n2){
  print(ks.test(n1[['anger_stsc']], n2[['anger_stsc']]))
  print(ks.test(n1[['disgust_stsc']], n2[['disgust_stsc']]))
  print(ks.test(n1[['joy_stsc']], n2[['joy_kw']]))
  print(ks.test(n1[['sadness_stsc']], n2[['sadness_stsc']]))
  print(ks.test(n1[['fear_stsc']], n2[['fear_stsc']]))
}
KStest(HLT, LHF)

# T-F
T_news = subset(stsc_data, false==0 & emo_prob_stsc!='-1')
F_news = subset(stsc_data, false==1 & emo_prob_stsc!='-1')
KStest(T_news, F_news)

# L-H
L_news = subset(stsc_data, label=='LT' & emo_prob_stsc!='-1' | label=='LF' & emo_prob_stsc!='-1')
H_news = subset(stsc_data, label=='HT' & emo_prob_stsc!='-1' | label=='HF' & emo_prob_stsc!='-1')
KStest(L_news, H_news)
###################################################################################################


covid_data = read.csv('data/covid_19_R.csv')

covid_data$diff = covid_data$anger - covid_data$joy
H = subset(covid_data, repostnum>=10)
L = subset(covid_data, repostnum<10)
sub = subset(covid_data, anger>0)
ks.test(H$diff, L$diff)
ks.test(H$joy, L$joy)
t.test(H$diff, L$diff, paired=T)
ks.test(H$anger, sub$anger)
