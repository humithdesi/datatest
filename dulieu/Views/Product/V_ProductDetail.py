from itertools import count
import re
from django.shortcuts import render,redirect
from django.http import Http404
from platformdirs import user_cache_dir
from ...Models.M_Product import Product,Review,LikeProduct
from django.http import HttpResponse,Http404,JsonResponse

def ProductDetail(request, slug):
    if request.method=='POST':
       #Post Comment
        likeProduct=Product.objects.get(slug=slug)
        productCommnet=Product.objects.get(slug=slug)
        user=request.user
        Comment=request.POST.get('comment')
        if Comment:
            review=Review(product=productCommnet,user=user,comment=Comment)
            review.save()
            text='/sanpham/'+str(slug)
            return redirect(text)
        else:
            pass
        Likes=request.POST.get('like')
        likeFill= likeProduct.likes.all().filter(user=user)
        likeAll=likeProduct.likes.all()
        listLike=[str(i.user) for i in likeAll ]
        if Likes:
            try:
                if str(user) in listLike: 
                    for i in likeFill:
                        print(i.user)
                        i.delete()
                    for x in likeAll:
                        print(x.user)       
                    print()
                    if str(likeAll.count()-1)=='0':
                        alertLike='hãy là người đầu tiên thích sản phẩm này'
                    else:    
                        alertLike=str(likeAll.count()-1)+" người khác đã thích sản phẩm này"          
                    return JsonResponse({'like':alertLike})
                else:
                    like=LikeProduct(product=likeProduct,user=user,like=True)   
                    like.save()
                    if str(len(listLike))=='0':
                        alertLike='bạn đã thích sản phẩm này'
                    else:
                        alertLike='bạn và: '+str(len(listLike))+" người khác đã thích sản phẩm này"   
                    return JsonResponse({'like':alertLike})
            except:
                pass    
        else:
            pass    
        print(Comment)
        print('test')
        
    else:
        try:
            product= Product.objects.get(slug=slug) 
            product.count_view +=1
            product.save()
            print(product.count_view)
            sizes=product.kichThuoc.all()
            dodays=product.doDay.all()
            products=Product.objects.all()
            comments = product.comments.all()# product.relate_name.all() truy vấn liên quan đến khóa chính product
            likes=product.likes.all()
            user=request.user
            listLike=[str(i.user) for i in likes ]
            if str(user) in listLike:
                if str(likes.count()-1)=='0':
                    alertLike='bạn đã thích sản phẩm này'
                else :
                    alertLike='bạn và '+ str(likes.count()-1)+' người khác thích sản phẩm này'
            elif str(likes.count())=='0':
                alertLike='hãy là người đầu tiên thích sản phẩm này'
            else:
                alertLike=str(likes.count())+' người thích sản phẩm này'    

        except Product.DoesNotExist:
            raise Http404('Sản Phẩm Không Tồn tại')
        content={
        'product': product,
        'sizes':sizes,
        'dodays':dodays,
        'products':products,
        'comments':comments,
        'likes':alertLike
        }    

        return render(request, 'dulieu/Product/ProductDetail.htm', content)