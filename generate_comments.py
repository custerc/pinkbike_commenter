# doesn't work, some kind of tf error

import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

single_comment = gpt2.generate(sess, return_as_list=True)[0]
print(single_text)
