# Copyright 2024 Google LLC
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
#


"""Test files get method."""

import pytest
from ... import types
from .. import pytest_helper

test_table: list[pytest_helper.TestTableItem] = [
    pytest_helper.TestTableItem(
        name='test_get',
        parameters=types._GetFileParameters(name='files/vjvu9fwk2qj8'),
        exception_if_vertex='only supported in the Gemini Developer client',
    ),
]

pytestmark = pytest_helper.setup(
    file=__file__,
    globals_for_file=globals(),
    test_method='files.get',
    test_table=test_table,
)


@pytest.mark.asyncio
async def test_async(client):
  with pytest_helper.exception_if_vertex(client, ValueError):
    file = await client.aio.files.get(name='files/vjvu9fwk2qj8')
