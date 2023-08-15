# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import json
from dataclasses import dataclass, field


@dataclass
class Segment:
    index: int = 0
    content: list = field(default_factory=list)
    finished: bool = False
    is_empty: bool = False
    data_type: str = None
    tgt_lang: str = ""

    def json(self) -> str:
        info_dict = {attribute: value for attribute, value in self.__dict__.items()}
        return json.dumps(info_dict)

    @classmethod
    def from_json(cls, json_string: str):
        return cls(**json.loads(json_string))


@dataclass
class EmptySegment(Segment):
    is_empty: bool = True


@dataclass
class TextSegment(Segment):
    content: str = ""
    data_type: str = "text"
    tgt_lang: str = ""


@dataclass
class SpeechSegment(Segment):
    sample_rate: int = -1
    data_type: str = "speech"
    tgt_lang: str = ""


def segment_from_json_string(string: str):
    info_dict = json.loads(string)
    if info_dict["data_type"] == "text":
        return TextSegment.from_json(string)
    elif info_dict["data_type"] == "speech":
        return SpeechSegment.from_json(string)
    else:
        return EmptySegment.from_json(string)

# Create a TextSegment from a string

# output = segment_from_json_string('{"index": 0, "content": "hello world", "finished": false, "is_empty": false, "data_type": "speech", "tgt_lang": ["en", "es", "fr"]}')
# print(output)

# txt = text_segment_from_string("hello world", "en")
# print(txt)

# txt = text_segment_from_string("hello world")