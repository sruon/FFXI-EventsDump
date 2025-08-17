# 17875357 - Scalable Area

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Sih Gates (ID: 268) |
| Block Size       | 436 bytes           |
| Total Events     | 2                   |
| References Count | 30                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [18](#event-18)       | 0x0001       |    290 |             49 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x095F      |        2399 |
|       1 | 0x0954      |        2388 |
|       2 | 0x1EC4      |        7876 |
|       3 | 0x1EC5      |        7877 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x00C8      |         200 |
|       7 | 0x0013      |          19 |
|       8 | 0xFFFCA40C  |  4294747148 |
|       9 | 0xFFFADDA1  |  4294630817 |
|      10 | 0xFFFFD97A  |  4294957434 |
|      11 | 0xFFFFFBB4  |  4294966196 |
|      12 | 0x0002      |           2 |
|      13 | 0xFFFCA4E9  |  4294747369 |
|      14 | 0xFFFAC4EB  |  4294624491 |
|      15 | 0xFFFFB24E  |  4294947406 |
|      16 | 0x03E8      |        1000 |
|      17 | 0x0003      |           3 |
|      18 | 0xFFFC09DC  |  4294707676 |
|      19 | 0xFFFB7C44  |  4294671428 |
|      20 | 0xFFFFD95E  |  4294957406 |
|      21 | 0xFFFFFC18  |  4294966296 |
|      22 | 0x0004      |           4 |
|      23 | 0xFFFC097B  |  4294707579 |
|      24 | 0xFFFB6255  |  4294664789 |
|      25 | 0xFFFFB208  |  4294947336 |
|      26 | 0x0384      |         900 |
|      27 | 0x001E      |          30 |
|      28 | 0x000F      |          15 |
|      29 | 0x40000000  |  1073741824 |

## String References

- **7876**: You might be able to [descend/ascend] using these vines if you only had $3 and $6.
- **7877**: [Descend/Ascend]? [Yes./No.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 290 bytes |
| Instructions | 49        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 05 10 00 80 03 06  10 01 80 48 02 80 23 24   ..........H..#$
0010: 03 80 04 80 04 80 25 02  00 10 04 80 00 11 01 42  ......%........B
0020: 03 01 10 05 80 43 00 43  01 4A F0 FF FF 7F F8 FF  .....C.C.J......
0030: FF 7F 6F 76 F0 FF FF 7F  45 06 80 F0 FF FF 7F F0  ..ov....E.......
0040: FF FF 7F 66 64 6F 31 04  80 55 06 80 F0 FF FF 7F  ...fdo1..U......
0050: F0 FF FF 7F 66 64 6F 31  38 07 80 02 07 10 05 80  ....fdo18.......
0060: 80 7F 00 BA F0 FF FF 7F  08 80 09 80 0A 80 0B 80  ................
0070: 47 00 08 80 09 80 0A 80  0B 80 47 01 01 EB 00 02  G.........G.....
0080: 07 10 0C 80 80 A3 00 BA  F0 FF FF 7F 0D 80 0E 80  ................
0090: 0F 80 10 80 47 00 0D 80  0E 80 0F 80 10 80 47 01  ....G.........G.
00A0: 01 EB 00 02 07 10 11 80  80 C7 00 BA F0 FF FF 7F  ................
00B0: 12 80 13 80 14 80 15 80  47 00 12 80 13 80 14 80  ........G.......
00C0: 15 80 47 01 01 EB 00 02  07 10 16 80 80 EB 00 BA  ..G.............
00D0: F0 FF FF 7F 17 80 18 80  19 80 1A 80 47 00 17 80  ............G...
00E0: 18 80 19 80 1A 80 47 01  01 EB 00 1C 1B 80 80 F0  ......G.........
00F0: FF FF 7F 1C 1C 80 AB 11  04 80 1C 05 80 45 06 80  .............E..
0100: F0 FF FF 7F F0 FF FF 7F  66 64 69 32 04 80 01 21  ........fdi2...!
0110: 01 02 00 10 05 80 00 21  01 03 01 10 1D 80 01 21  .......!.......!
0120: 01 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[5] = 2399*
  1: 0x0006 [0x03] Work_Zone[6] = 2388*
  2: 0x000B [0x48] [System] [7876*]:
    → "You might be able to [descend/ascend] using these vines if you only had $3 and $6."
  3: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000F [0x24] CREATE_DIALOG(message_id=7877*, default_option=0*, option_flags=0*)
    → "[Descend/Ascend]? [Yes./No.]"
  5: 0x0016 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0017 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0111
  7: 0x001F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x0020 [0x03] Work_Zone[1] = 1*
  9: 0x0025 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0027 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0029 [0x4A] LocalPlayer looks at EventEntity
 12: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x0033 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 14: 0x0038 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0049 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 16: 0x0058 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 17: 0x005B [0x02] IF !(Work_Zone[7] == 1*) GOTO 0x007F
 18: 0x0063 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-220.148*, pos_z=-336.479*, pos_y=-9.862*, direction=377476122.5°*)
 19: 0x0070 [0x47] UPDATE_PLAYER_POS(-220.148*, -336.479*, -9.862*, yaw=377476122.5°*)
 20: 0x007A [0x47] WAIT_PLAYER_POS_UPDATE
 21: 0x007C [0x01] GOTO 0x00EB
 22: 0x007F [0x02] IF !(Work_Zone[7] == 2*) GOTO 0x00A3
 23: 0x0087 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-219.927*, pos_z=-342.805*, pos_y=-19.890*, direction=87.9°*)
 24: 0x0094 [0x47] UPDATE_PLAYER_POS(-219.927*, -342.805*, -19.890*, yaw=87.9°*)
 25: 0x009E [0x47] WAIT_PLAYER_POS_UPDATE
 26: 0x00A0 [0x01] GOTO 0x00EB
 27: 0x00A3 [0x02] IF !(Work_Zone[7] == 3*) GOTO 0x00C7
 28: 0x00AB [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-259.620*, pos_z=-295.868*, pos_y=-9.890*, direction=377476131.3°*)
 29: 0x00B8 [0x47] UPDATE_PLAYER_POS(-259.620*, -295.868*, -9.890*, yaw=377476131.3°*)
 30: 0x00C2 [0x47] WAIT_PLAYER_POS_UPDATE
 31: 0x00C4 [0x01] GOTO 0x00EB
 32: 0x00C7 [0x02] IF !(Work_Zone[7] == 4*) GOTO 0x00EB
 33: 0x00CF [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-259.717*, pos_z=-302.507*, pos_y=-19.960*, direction=79.1°*)
 34: 0x00DC [0x47] UPDATE_PLAYER_POS(-259.717*, -302.507*, -19.960*, yaw=79.1°*)
 35: 0x00E6 [0x47] WAIT_PLAYER_POS_UPDATE
 36: 0x00E8 [0x01] GOTO 0x00EB

SUBROUTINE_00EB:
 37: 0x00EB [0x1C] WAIT(30* ticks)
 38: 0x00EE [0x80] LOAD_WAIT(entity=LocalPlayer)
 39: 0x00F3 [0x1C] WAIT(15* ticks)
 40: 0x00F6 [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
 41: 0x00FA [0x1C] WAIT(1* ticks)
 42: 0x00FD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x010E [0x01] GOTO 0x0121
 44: 0x0111 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0121
 45: 0x0119 [0x03] Work_Zone[1] = 1073741824*
 46: 0x011E [0x01] GOTO 0x0121

SUBROUTINE_0121:
 47: 0x0121 [0x21] END_EVENT
 48: 0x0122 [0x00] END_REQSTACK()
```
