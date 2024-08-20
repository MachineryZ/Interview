智能指针有多少种

- unique_ptr
  - 独占所有权：每个 std::unique_ptr 实例





还是要麻烦amax的同学制作一下镜像

1. 集群里dockerfile 的上传方式有报错，而且集群不联网，dockerfile无法离线制作镜像
2. 本地制作镜像，目前都是windows系统配合wsl办公，制作镜像的时候有一些环境上和测试上的问题
3. 不仅仅是pyarrow的包（单个包还是可以偶尔手动下载）还有一些其他的库依赖，一个一个手动下载上传实在是不方便
4. 需要以下几个包的 pip instal 命令加入到 pytorch 环境里
   1. pyarrow（最新版本）
   2. py3nvml （最新版本）
   3. pandas_market_calendars（最新版本）
   4. matplotlib（最新版本）
   5. tqdm（最新版本）
   6. xgboost（最新版本）
   7. lightbgm（最新版本）
5. （pytorch镜像已经有conda版本，不需要额外安装conda）
6. base镜像为集群镜像中名称为 "pytorch，tag为 2.1.2-conda-cuda12.1-cudnn8-ubuntu20.04"

这次还是麻烦一下amax的同学更新上传一下满足以上要求的pytorch镜像，之后会走通我们这边自己上传的镜像流程

然后麻烦给一下anaconda，pytorch，r-base镜像的dockerfile内容（如果是基于 dockerfile 的形式制作的话）以供参考