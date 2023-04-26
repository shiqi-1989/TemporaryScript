import subprocess
from datetime import datetime
from multiprocessing.pool import ThreadPool
import requests

THREADING_NUM = 10
pool = ThreadPool(THREADING_NUM)

num = 1


def pingFun(Domain):
    global num
    command = f"ping {Domain} -c 1"
    # p = subprocess.Popen(command,
    #                      stdout=subprocess.PIPE,
    #                      stdin=subprocess.PIPE,
    #                      stderr=subprocess.PIPE,
    #                      shell=True,
    #                      encoding='gbk')
    # p.wait()
    # result = p.stdout.readlines()[0]

    p = subprocess.run(command,
                       stdout=subprocess.PIPE,
                       stdin=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       shell=True,
                       encoding='utf-8')
    if p.returncode == 0:
        result = p.stdout.split('\n', 1)[0]
        if "wswebcdn.com" in result:
            url = f"https://{Domain.strip()}"
            res = requests.get(url, timeout=5)
            print(f"{num}:{Domain} \n匹配成功！: {result}")
            if res.status_code == 200:
                print(f"{res.status_code}: 验证通过 \n")
            else:
                print(f"{res.status_code}: 验证失败 \n")
        else:
            print(f"{num}:{Domain} \n匹配失败！: {result}\n")
        # time.sleep(0.5)
    else:
        print(f"{num}:{Domain} error \n")
    num += 1


if __name__ == '__main__':
    start_time = datetime.now()
    cmds = """aba.huatu.com
    ah.huatu.com
    akesu.huatu.com
    alashan.huatu.com
    aletai.huatu.com
    ankang.huatu.com
    anqing.huatu.com
    anshan.huatu.com
    anshun.huatu.com
    anyang.huatu.com
    ask.huatu.com
    baicheng.huatu.com
    baise.huatu.com
    baishan.huatu.com
    baiyin.huatu.com
    banna.huatu.com
    baoding.huatu.com
    baoji.huatu.com
    baoshan.huatu.com
    baotou.huatu.com
    bayuquan.huatu.com
    bazhong.huatu.com
    beihai.huatu.com
    beipiao.huatu.com
    bengbu.huatu.com
    benxi.huatu.com
    bijie.huatu.com
    bingtuan.huatu.com
    binzhou.huatu.com
    bj.huatu.com
    bole.huatu.com
    bozhou.huatu.com
    byne.huatu.com
    caigou.huatu.com
    cangzhou.huatu.com
    changchun.huatu.com
    changde.huatu.com
    changji.huatu.com
    changsha.huatu.com
    changzhi.huatu.com
    changzhou.huatu.com
    chaohu.huatu.com
    chaoyang.huatu.com
    chaozhou.huatu.com
    chengde.huatu.com
    chengdu.huatu.com
    chenggong.huatu.com
    chengnan.huatu.com
    chenzhou.huatu.com
    chifeng.huatu.com
    chizhou.huatu.com
    chongzuo.huatu.com
    chuxiong.huatu.com
    chuzhou.huatu.com
    cq.huatu.com
    cunguan.huatu.com
    dali.huatu.com
    dalian.huatu.com
    dandong.huatu.com
    danzhou.huatu.com
    daqing.huatu.com
    dashiqiao.huatu.com
    datong.huatu.com
    dazhou.huatu.com
    dehong.huatu.com
    dengta.huatu.com
    deyang.huatu.com
    dezhou.huatu.com
    dingxi.huatu.com
    diqing.huatu.com
    dongfang.huatu.com
    dongguan.huatu.com
    dongying.huatu.com
    doufen.huatu.com
    duyun.huatu.com
    dxal.huatu.com
    eeds.huatu.com
    enshi.huatu.com
    ezhou.huatu.com
    fangchenggang.huatu.com
    file.huatu.com
    fj.huatu.com
    foshan.huatu.com
    fushun.huatu.com
    fuxin.huatu.com
    fuyang.huatu.com
    fuzhou.huatu.com
    fzhou.huatu.com
    gannan.huatu.com
    ganzhou.huatu.com
    ganzi.huatu.com
    gaoguan.huatu.com
    gd.huatu.com
    gk.huatu.com
    gs.huatu.com
    guangan.huatu.com
    guangyuan.huatu.com
    guangzhou.huatu.com
    guigang.huatu.com
    guilin.huatu.com
    guiyang.huatu.com
    guyuan.huatu.com
    gx.huatu.com
    gxg.huatu.com
    gz.huatu.com
    ha.huatu.com
    haerbin.huatu.com
    haian.huatu.com
    haikou.huatu.com
    haixi.huatu.com
    hami.huatu.com
    handan.huatu.com
    hangzhou.huatu.com
    hanzhong.huatu.com
    hb.huatu.com
    he.huatu.com
    hebi.huatu.com
    hechi.huatu.com
    hedong.huatu.com
    hefei.huatu.com
    hegang.huatu.com
    heihe.huatu.com
    hengshui.huatu.com
    hengyang.huatu.com
    hetian.huatu.com
    hexi.huatu.com
    heyuan.huatu.com
    heze.huatu.com
    hezhou.huatu.com
    hhht.huatu.com
    hi.huatu.com
    hlbr.huatu.com
    hlj.huatu.com
    hn.huatu.com
    honghe.huatu.com
    huaian.huatu.com
    huaibei.huatu.com
    huaihua.huatu.com
    huainan.huatu.com
    huanggang.huatu.com
    huangshan.huatu.com
    huangshi.huatu.com
    huizhou.huatu.com
    huludao.huatu.com
    huzhou.huatu.com
    jiamusi.huatu.com
    jian.huatu.com
    jiangbei.huatu.com
    jiangmen.huatu.com
    jiaoshi.huatu.com
    jiaozuo.huatu.com
    jiaxing.huatu.com
    jiayuguan.huatu.com
    jieyang.huatu.com
    jinan.huatu.com
    jinchang.huatu.com
    jincheng.huatu.com
    jingdezhen.huatu.com
    jingmen.huatu.com
    jingyue.huatu.com
    jingzhou.huatu.com
    jinhua.huatu.com
    jining.huatu.com
    jinrong.huatu.com
    jinzhong.huatu.com
    jinzhou.huatu.com
    jiujiang.huatu.com
    jiuquan.huatu.com
    jixi.huatu.com
    jiyuan.huatu.com
    jl.huatu.com
    jls.huatu.com
    js.huatu.com
    jx.huatu.com
    jzg.huatu.com
    kaifeng.huatu.com
    kaili.huatu.com
    kaiyuan.huatu.com
    kashi.huatu.com
    klmy.huatu.com
    kuerle.huatu.com
    kunming.huatu.com
    laibin.huatu.com
    laiwu.huatu.com
    langfang.huatu.com
    lanzhou.huatu.com
    lasa.huatu.com
    leshan.huatu.com
    liangshan.huatu.com
    lianyungang.huatu.com
    liaocheng.huatu.com
    liaoyang.huatu.com
    liaoyuan.huatu.com
    lijiang.huatu.com
    lincang.huatu.com
    linfen.huatu.com
    lingyuan.huatu.com
    linxia.huatu.com
    linyi.huatu.com
    lishui.huatu.com
    liupanshui.huatu.com
    liuzhou.huatu.com
    ln.huatu.com
    longnan.huatu.com
    longyan.huatu.com
    loudi.huatu.com
    luan.huatu.com
    luohe.huatu.com
    luoyang.huatu.com
    luzhou.huatu.com
    lvliang.huatu.com
    maanshan.huatu.com
    maoming.huatu.com
    meishan.huatu.com
    meizhou.huatu.com
    mianyang.huatu.com
    mudanjiang.huatu.com
    nanchang.huatu.com
    nanchong.huatu.com
    nanjing.huatu.com
    nanning.huatu.com
    nanping.huatu.com
    nantong.huatu.com
    nanyang.huatu.com
    neijiang.huatu.com
    ningbo.huatu.com
    ningde.huatu.com
    ningjin.huatu.com
    nmg.huatu.com
    nujiang.huatu.com
    nx.huatu.com
    panjin.huatu.com
    panzhihua.huatu.com
    photo.huatu.com
    pingdingshan.huatu.com
    pinghu.huatu.com
    pingliang.huatu.com
    pingxiang.huatu.com
    pixian.huatu.com
    puer.huatu.com
    putian.huatu.com
    puyang.huatu.com
    qh.huatu.com
    qianan.huatu.com
    qianjiang.huatu.com
    qidong.huatu.com
    qingdao.huatu.com
    qingyang.huatu.com
    qingyuan.huatu.com
    qinhuangdao.huatu.com
    qinzhou.huatu.com
    qionghai.huatu.com
    qitaihe.huatu.com
    qqhe.huatu.com
    quanzhou.huatu.com
    qujing.huatu.com
    quzhou.huatu.com
    record.huatu.com
    rizhao.huatu.com
    ruijin.huatu.com
    sanmenxia.huatu.com
    sanming.huatu.com
    sanya.huatu.com
    sc.huatu.com
    sd.huatu.com
    sh.huatu.com
    shangluo.huatu.com
    shangqiu.huatu.com
    shangrao.huatu.com
    shantou.huatu.com
    shanwei.huatu.com
    shaoguan.huatu.com
    shaoxing.huatu.com
    shaoyang.huatu.com
    shenbei.huatu.com
    shenyang.huatu.com
    shenzhen.huatu.com
    shexian.huatu.com
    shihezi.huatu.com
    shijiazhuang.huatu.com
    shiyan.huatu.com
    shizuishan.huatu.com
    shuangshi.huatu.com
    shuangyashan.huatu.com
    shuozhou.huatu.com
    shuyang.huatu.com
    siping.huatu.com
    sitemgt.oss.huatu.com
    sn.huatu.com
    snj.huatu.com
    songyuan.huatu.com
    suihua.huatu.com
    suining.huatu.com
    suizhou.huatu.com
    suqian.huatu.com
    suzhou.huatu.com
    sx.huatu.com
    sydw.huatu.com
    szhou.huatu.com
    tacheng.huatu.com
    taian.huatu.com
    taiyuan.huatu.com
    taizhou.huatu.com
    tangshan.huatu.com
    tengzhou.huatu.com
    tianmen.huatu.com
    tianshui.huatu.com
    tieling.huatu.com
    tj.huatu.com
    tongchuan.huatu.com
    tonghua.huatu.com
    tongliao.huatu.com
    tongling.huatu.com
    tongren.huatu.com
    tt.huatu.com
    tulufan.huatu.com
    tzhou.huatu.com
    u1.huatu.com
    u2.huatu.com
    u3.huatu.com
    wafang.huatu.com
    wanning.huatu.com
    weifang.huatu.com
    weihai.huatu.com
    weinan.huatu.com
    wenchang.huatu.com
    wenjiang.huatu.com
    wenshan.huatu.com
    wenzhou.huatu.com
    wlcb.huatu.com
    wlmq.huatu.com
    wuhai.huatu.com
    wuhan.huatu.com
    wuhu.huatu.com
    wujiaqu.huatu.com
    wuwei.huatu.com
    wuxi.huatu.com
    wuzhishan.huatu.com
    wuzhong.huatu.com
    wuzhou.huatu.com
    www.huatu.com
    xds.huatu.com
    xiamen.huatu.com
    xian.huatu.com
    xiangtan.huatu.com
    xiangxi.huatu.com
    xiangyang.huatu.com
    xianning.huatu.com
    xiantao.huatu.com
    xianyang.huatu.com
    xiaogan.huatu.com
    xingan.huatu.com
    xingtai.huatu.com
    xingyi.huatu.com
    xining.huatu.com
    xinji.huatu.com
    xinxiang.huatu.com
    xinyang.huatu.com
    xinyu.huatu.com
    xinzhou.huatu.com
    xj.huatu.com
    xlgl.huatu.com
    xuancheng.huatu.com
    xuchang.huatu.com
    xue.huatu.com
    xuzhou.huatu.com
    xz.huatu.com
    yaan.huatu.com
    yanan.huatu.com
    yanbian.huatu.com
    yancheng.huatu.com
    yangjiang.huatu.com
    yangquan.huatu.com
    yangzhou.huatu.com
    yantai.huatu.com
    ychun.huatu.com
    yibin.huatu.com
    yichang.huatu.com
    yichun.huatu.com
    yili.huatu.com
    yinchuan.huatu.com
    yingkou.huatu.com
    yingtan.huatu.com
    yiyang.huatu.com
    ylin.huatu.com
    ylws.huatu.com
    yn.huatu.com
    yongzhou.huatu.com
    yueyang.huatu.com
    yulin.huatu.com
    yuncheng.huatu.com
    yunfu.huatu.com
    yushu.huatu.com
    yuxi.huatu.com
    zaozhuang.huatu.com
    zd.huatu.com
    zfgj.huatu.com
    zhangjiajie.huatu.com
    zhangjiakou.huatu.com
    zhangwu.huatu.com
    zhangye.huatu.com
    zhangzhou.huatu.com
    zhanjiang.huatu.com
    zhaojing.huatu.com
    zhaoqing.huatu.com
    zhaotong.huatu.com
    zhengzhou.huatu.com
    zhenjiang.huatu.com
    zhongshan.huatu.com
    zhongwei.huatu.com
    zhoukou.huatu.com
    zhoushan.huatu.com
    zhuhai.huatu.com
    zhumadian.huatu.com
    zhuzhou.huatu.com
    zibo.huatu.com
    zigong.huatu.com
    ziyang.huatu.com
    zj.huatu.com
    zt-disk.huatu.com
    zunyi.huatu.com
    zw.huatu.com
    zwsearch.huatu.com
    xd.huatu.com
    m.xue.huatu.com"""
    for Domain in cmds.split("\n"):
        # pingFun(Domain)
        pool.apply_async(pingFun, (Domain,))
    pool.close()
    pool.join()
    end_time = datetime.now()
    print('All done.总花费时间{:0.2f}s.'.format((end_time - start_time).total_seconds()))
