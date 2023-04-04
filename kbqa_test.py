#!/usr/bin/env python3
# coding: utf-8

from entity_extractor import EntityExtractor
from search_answer import AnswerSearching


class KBQA:
    def __init__(self):
        self.extractor = EntityExtractor()
        self.searcher = AnswerSearching()

    def qa_main(self, input_str):
        answer = "对不起，您的问题我不知道，我今后会努力改进的。"
        entities = self.extractor.extractor(input_str)
        # TIPS: 这个entities可以print一下看看效果
        if not entities:
            return answer
        # 主要是根据不同的实体和意图构造cypher查询语句
        sqls = self.searcher.question_parser(entities)
        # 执行cypher查询，返回结果
        final_answer = self.searcher.searching(sqls)
        if not final_answer:
            # 没找到答案，默认回答
            return answer
        else:
            return '\n'.join(final_answer)


if __name__ == "__main__":
    handler = KBQA()
    while True:
        question = input("用户：")
        if not question:
            break
        answer = handler.qa_main(question)
        print("小豪：", answer)
        print("*"*50)
