# coding=utf-8
# Copyright 2018-2022 EVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from eva.parser.evaql.evaql_parser import evaql_parser
from eva.parser.evaql.evaql_parserVisitor import evaql_parserVisitor
from eva.parser.select_like_statement import SelectLikeStatement
from eva.parser.table_ref import TableRef


##################################################################
# SELECT LIKE STATEMENT
##################################################################
class SelectLike(evaql_parserVisitor):
    def visitSelectLikeStatement(self, ctx: evaql_parser.SelectLikeStatementContext):
        table_ref = TableRef(self.visitTableName(ctx.tableName()))
        target_img = ctx.fileName()

        return SelectLikeStatement(table_ref, target_img)