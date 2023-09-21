import json
import os
import shutil
import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from MEDI.settings import project_path
from backend.service import train_model_service

@csrf_exempt
@require_http_methods(["GET"])
def get_all_models(request):
    models = train_model_service.get_all_models()
    return HttpResponse(json.dumps(models), content_type="application/json")

@csrf_exempt
@require_http_methods(["POST"])
def upload_medical_archive(request):
    return HttpResponse("TODO")
    # model_name = request.POST.get('modelName')
    # ques = request.POST.get('desc')
    # file = request.FILES.get('file')
    # print("upload imag to ai robot. Model: "+model_name);
    # upload_path = project_path + "uploadimag"
    # # 生成15位随机字母数字字符串
    # random_alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # random_str = ''.join(random.choice(random_alphanumeric) for _ in range(15))
    #
    # file_name = file.name
    # file_path = os.path.join(upload_path, random_str + file_name[-4:])
    # print(file_path)
    #
    # # 判断父级目录是否存在
    # if not os.path.exists(upload_path):
    #     os.makedirs(upload_path)
    #
    # try:
    #     with open(upload_path, 'wb+') as f:
    #         for chunk in file.chunks():
    #             f.write(chunk)
    #     os.rename(upload_path+file_name, upload_path+random_str+file_name[-4:])
    #     print(upload_path+random_str+file_name[-4:])
    #     return HttpResponse("success")
    # except IOError as e:
    #     print(e)
    #     return HttpResponse("error", status=400)


# //这里改成post图片和问题，调用python回答问题，res是answer,输入是图片的arr和ques
# @PostMapping("/archive/user/{modelName}")
# public Object uploadMedicalArchive(HttpServletResponse response, @RequestParam("desc") String ques, @RequestParam("file") MultipartFile file,
# @PathVariable String modelName) throws IOException {
#     System.out.println("upload imag to ai robot. Model: "+modelName);
# // 设置本地保存地址
# String projPath=(new File("")).getCanonicalPath();
# String uploadPath=projPath+"/uploadimag";
# String random = RandomStringUtils.randomAlphanumeric(15);
# // 文件保存url  这是保留前台上传文件的后缀(也可以在这里做文件格式的效验)
# File path = new File(uploadPath, random + file.getOriginalFilename().substring(file.getOriginalFilename().length() - 4));
# // 判断父级目录是否存在
# if (!path.getParentFile().exists()) {
#     path.getParentFile().mkdir();
# }
# // 文件对拷
# try {
# file.transferTo(path);
# // 成功返回前台数据
# System.out.println( uploadPath+'/'+ path.getName());
# //            return folder+'/'+ path.getName();
# } catch (IOException e) {
# e.printStackTrace();
# }
# String ans="ans null";
# Runtime run = Runtime.getRuntime();
# String imgpath=uploadPath+'/'+ path.getName();
# String question=ques;
# ReportPo reportPo=trainModelService.getReportPo(modelName);
# //        String savePath=(new File("")).getCanonicalPath()+"/weights";
# switch (reportPo.getClassification()){
# case "VGG-Seq2Seq":
# System.out.println("will predict seq2seq.");
# //call vgg seq2seq
# try{
# ans=pythonCallEntity.VGG_Seq2Seq_predict(reportPo.getName(), reportPo.getData(),
# imgpath, question , reportPo.getSavepath());
# System.out.println(ans);
# //                    ReportPo reportPo1_vgg=trainModelService.updateReportBleuByName(reportPo.getName(),Float.parseFloat(res));
#
# }catch (Exception e){
# e.printStackTrace();
# trainModelService.setTrainError(reportPo.getName());
# }
# break;
# case "NLM":
# System.out.println("will predict nlm.");
# //call NLM
# try{
# ans=pythonCallEntity.NLM_predict( reportPo.getName(), question, imgpath,reportPo.getData(),reportPo.getSavepath(),reportPo.getBatchsize());
# //                    ReportPo reportPo1_nlm=trainModelService.updateReportBleuByName(reportPo.getName(),Float.parseFloat(res));
# }catch (Exception e){
# e.printStackTrace();
# trainModelService.setTrainError(reportPo.getName());
# }
# break;
# case "ODL":
# System.out.println("will predict odl.");
#
# try{
# String ae="";
# String maml="";
# if(reportPo.getConstructor().equals("both")){
# ae="True";
# maml="True";
# }else if(reportPo.getConstructor().equals("maml")){
# ae="False";
# maml="True";
# }else if(reportPo.getConstructor().equals("none")){
# ae="False";
# maml="False";
# }else {
# ae="True";
# maml="False";
# }
#
# ans=pythonCallEntity.ODL_predict(reportPo.getName(),question,imgpath,reportPo.getSavepath(),
# reportPo.getAttention(),reportPo.getRnnCell(),ae,maml,reportPo.getData());
# }catch (Exception e){
# e.printStackTrace();
# trainModelService.setTrainError(reportPo.getName());
# }
# break;
# case "MMBERT":
# System.out.println("will predict mmbert.");
# //call mmbert python
# ans=pythonCallEntity.MMBERT_predict(reportPo.getName(),question,imgpath,reportPo.getSavepath(),reportPo.getData());
# break;
# default:
# System.out.println("this model unsupported.");
# return "fail.";
# }
# return ans;
# }
# }
