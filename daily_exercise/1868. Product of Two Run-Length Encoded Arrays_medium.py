class Solution:
    def findRLEArray_W(self, encoded1, encoded2):

        res = []
        encoded1.reverse()
        encoded2.reverse()
        while encoded1 != [] and encoded2 != []:
            print('res: ', res,  '\n',
                  'e1: ', list(reversed(encoded1)), '\n',
                  'e2: ', list(reversed(encoded2))
                  )
            val_1, freq_1 = encoded1.pop()
            val_2, freq_2 = encoded2.pop()
            if freq_1 < freq_2:
                res.append([val_1 * val_2, freq_1])
                encoded2.append([val_2, freq_2 - freq_1])
            elif freq_1 > freq_2:
                res.append([val_1 * val_2, freq_2])
                encoded1.append([val_1, freq_1 - freq_2])
            else:
                res.append([val_1 * val_2, freq_1])


        merged_res = []

        if len(res) >= 2:
            slow, fast = 0, 1
            while fast < len(res):
                freq = res[slow][1]
                if res[fast][0] == res[slow][0]:
                    freq += res[fast][1]
                    fast += 1
                else:
                    merged_res.append([res[slow][0], freq])
                    slow = fast
                    fast += 1

            if slow < len(res) - 1:
                merged_res.append([res[slow][0], freq])
            else:
                merged_res.append(res[slow])

        return merged_res

    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        product_encoded = []

        e1_index = 0
        e2_index = 0

        while e1_index < len(encoded1) and e2_index < len(encoded2):
            e1_val, e1_freq = encoded1[e1_index]
            e2_val, e2_freq = encoded2[e2_index]

            product_val = e1_val * e2_val
            product_freq = min(e1_freq, e2_freq)

            encoded1[e1_index][1] -= product_freq
            encoded2[e2_index][1] -= product_freq

            if encoded1[e1_index][1] == 0:
                e1_index += 1

            if encoded2[e2_index][1] == 0:
                e2_index += 1

            if not product_encoded or product_encoded[-1][0] != product_val:
                product_encoded.append([product_val, product_freq])
            else:
                product_encoded[-1][1] += product_freq

        return product_encoded

e1=[[5,2],[3,5],[5,4],[2,5],[3,4],[4,5],[1,2],[2,1],[3,1],[5,5]]
e2=[[2,5],[1,1],[2,1],[1,3],[5,2],[3,4],[2,5],[5,5],[4,2],[2,1],[1,4],[3,1]]

Solution().findRLEArray(e1, e2)