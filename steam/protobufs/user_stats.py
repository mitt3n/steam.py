# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_clientserver_userstats.proto
# plugin: python-betterproto
# Last updated 09/09/2021

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class CMsgClientGetUserStats(betterproto.Message):
    game_id: int = betterproto.fixed64_field(1)
    crc_stats: int = betterproto.uint32_field(2)
    schema_local_version: int = betterproto.int32_field(3)
    steam_id_for_user: int = betterproto.fixed64_field(4)


@dataclass(eq=False, repr=False)
class CMsgClientGetUserStatsResponse(betterproto.Message):
    game_id: int = betterproto.fixed64_field(1)
    eresult: int = betterproto.int32_field(2)
    crc_stats: int = betterproto.uint32_field(3)
    schema: bytes = betterproto.bytes_field(4)
    stats: List["CMsgClientGetUserStatsResponseStats"] = betterproto.message_field(5)
    achievement_blocks: List["CMsgClientGetUserStatsResponseAchievementBlocks"] = betterproto.message_field(6)


@dataclass(eq=False, repr=False)
class CMsgClientGetUserStatsResponseStats(betterproto.Message):
    stat_id: int = betterproto.uint32_field(1)
    stat_value: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientGetUserStatsResponseAchievementBlocks(betterproto.Message):
    achievement_id: int = betterproto.uint32_field(1)
    unlock_time: List[int] = betterproto.fixed32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientStoreUserStatsResponse(betterproto.Message):
    game_id: int = betterproto.fixed64_field(1)
    eresult: int = betterproto.int32_field(2)
    crc_stats: int = betterproto.uint32_field(3)
    stats_failed_validation: List["CMsgClientStoreUserStatsResponseStatsFailedValidation"] = betterproto.message_field(
        4
    )
    stats_out_of_date: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class CMsgClientStoreUserStatsResponseStatsFailedValidation(betterproto.Message):
    stat_id: int = betterproto.uint32_field(1)
    reverted_stat_value: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientStoreUserStats2(betterproto.Message):
    game_id: int = betterproto.fixed64_field(1)
    settor_steam_id: int = betterproto.fixed64_field(2)
    settee_steam_id: int = betterproto.fixed64_field(3)
    crc_stats: int = betterproto.uint32_field(4)
    explicit_reset: bool = betterproto.bool_field(5)
    stats: List["CMsgClientStoreUserStats2Stats"] = betterproto.message_field(6)


@dataclass(eq=False, repr=False)
class CMsgClientStoreUserStats2Stats(betterproto.Message):
    stat_id: int = betterproto.uint32_field(1)
    stat_value: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientStatsUpdated(betterproto.Message):
    steam_id: int = betterproto.fixed64_field(1)
    game_id: int = betterproto.fixed64_field(2)
    crc_stats: int = betterproto.uint32_field(3)
    updated_stats: List["CMsgClientStatsUpdatedUpdatedStats"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class CMsgClientStatsUpdatedUpdatedStats(betterproto.Message):
    stat_id: int = betterproto.uint32_field(1)
    stat_value: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CMsgClientStoreUserStats(betterproto.Message):
    game_id: int = betterproto.fixed64_field(1)
    explicit_reset: bool = betterproto.bool_field(2)
    stats_to_store: List["CMsgClientStoreUserStatsStatsToStore"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CMsgClientStoreUserStatsStatsToStore(betterproto.Message):
    stat_id: int = betterproto.uint32_field(1)
    stat_value: int = betterproto.uint32_field(2)
