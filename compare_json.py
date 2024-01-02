import json

def compare_json(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)

    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)

    # 比较两个JSON对象
    diff = compare_objects(data1, data2, 'root')
    # print('file1=',len(data1))
    # print('file2=',len(data2))
    amount = len(data2)
    accuracy_calculator(data1,amount,diff)
    
def accuracy_calculator(data1,amount,diff):
    x = 0
    items_amount = 0
    for i in data1.keys():
        field_count = len(data1[i])
        items_field_count = len(data1[i]["items"])
        items_amount += items_field_count
        x += field_count-1+items_field_count
    print("總欄位數目:", x)
    print_diff(diff)
    y = len(diff)
    acc = (x-y)/x*100
    print('acc= ',acc,'%')

    patient_record = {
            "nhi": amount,
            "admissionDate": amount,
            "dischargeDate": amount,
            "hospitalName": amount,
            "dept": amount,
            "receivedAmount": amount,  
            "items": items_amount  
            }
    # print('patient_record= ',patient_record)

    wrong_record = {
            "nhi": 0,
            "admissionDate": 0,
            "dischargeDate": 0,
            "hospitalName": 0,
            "dept": 0,
            "receivedAmount": 0,  
            "items": 0  
            }
    for record,values in diff.items():
        for i in wrong_record:
            if i in record:
                value = wrong_record.get(i)
                wrong_record[i]=value+1
    # print('wrong_record= ',wrong_record)
    total_avg =0
    print('Total_items_matrix:\nkeys\t\tN\tY\tSUM\tAVG')
    for i in patient_record.keys():
        correct= patient_record[i]-wrong_record[i]
        average = correct /patient_record[i]*100
        total_avg +=average
        key_name = f'{i:<10}' if len(i) < 10 else i
        print(f'{key_name}\t{wrong_record[i]}\t{correct}\t{patient_record[i]}\t{average:.2f}%')
    else:
        print(f'Total items accuracy AVG ={total_avg/7:.2f}%')
    
def compare_objects(obj1, obj2, path):
    diff = {}
    for key in obj1.keys() | obj2.keys():
        new_path = f'{path}.{key}' if path else key

        if key not in obj1:
            diff[new_path] = (None, obj2[key])
        elif key not in obj2:
            diff[new_path] = (obj1[key], None)
        elif isinstance(obj1[key], dict) and isinstance(obj2[key], dict):
            nested_diff = compare_objects(obj1[key], obj2[key], new_path)
            diff.update(nested_diff)
        elif obj1[key] != obj2[key]:
            diff[new_path] = (obj1[key], obj2[key])

    return diff

def print_diff(diff):
    if not diff:
        print("JSON文件相同")
    else:
        print("JSON文件不同的项：")
        for key, values in diff.items():
            print(f"{key}: {values[0]} -> {values[1]}")

if __name__ == "__main__":
    ## ntu , cg ,cch
    # file1_path = "ground_truth/ntu_ground_truth.json"
    # file2_path = "ntu_1117_14_mask.json"

    print("台大")
    file1_path = "ground_truth/ntu_ground_truth_line.json"
    file2_path = "1226/ntu_nana_cor1226.json"
    # # file2_path = "ntu_val_model.json"
    compare_json(file1_path, file2_path)
    # print("長庚")
    # file1_path = "ground_truth/cg_ground_truth.json"
    # # file2_path = "1120/cg_1120_mask.json"
    # file2_path = "1206/cg_warp.json"
    # compare_json(file1_path, file2_path)
    # print("彰基_old")
    # file1_path = "ground_truth/cch_ground_truth.json"
    # file2_path = "1120/yesu_1120.json"
    # compare_json(file1_path, file2_path)
    # print("彰基")
    # file1_path = "ground_truth/cch_ground_truth_line.json"
    # file2_path = "1120/magnify_cch1130.json"
    # compare_json(file1_path, file2_path)

    # file1_path = "ground_truth/ntu_ground_truth.json"
    # file2_path = "ntu_1120_18_b22.json"
    # file2_path = "model_output/cg_val_model.json"
    # file1_path ="ground_truth/ntu_cg_cch_gt.json"
    
    # file2_path = "model_output/cg_val_model.json"
    # file2_path = "model_output/ntu_val_model.json"
    
    # compare_json(file1_path, file2_path)



        