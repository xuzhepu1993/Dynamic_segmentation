load('raw_data.mat')

final=[];
for i=1:size(totalpoints,1)-1
    start_point=totalpoints(i);
    end_point=totalpoints(i+1);
    final(i,1)=start_point;
    final(i,2)=end_point;
    final(i,3)=111;
    
    
    status=[];
    for index_l1=1:size(L1,1)
        if start_point>=L1(index_l1,1)&&end_point<=L1(index_l1,2)
            status(size(status,1)+1)=111;
        end
    end
    
    for index_l2=1:size(L2,1)
        if start_point>=L2(index_l2,1)&&end_point<=L2(index_l2,2)
            status(size(status,1)+1)=112;
        end
    end
    
    for index_l3=1:size(L3,1)
        if start_point>=L3(index_l3,1)&&end_point<=L3(index_l3,2)
            status(size(status,1)+1)=113;
        end
    end
    
    for index_l4=1:size(L4,1)
        if start_point>=L4(index_l4,1)&&end_point<=L4(index_l4,2)
            status(size(status,1)+1)=121;
        end
    end
    
    for index_l5=1:size(L5,1)
        if start_point>=L5(index_l5,1)&&end_point<=L5(index_l5,2)
            status(size(status,1)+1)=122;
        end
    end
    
    for index_l6=1:size(L6,1)
        if start_point>=L6(index_l6,1)&&end_point<=L6(index_l6,2)
            status(size(status,1)+1)=123;
        end
    end
    
    if size(status)>0
         final(i,3)=max(status);
    end
    
       
    
    
    
end