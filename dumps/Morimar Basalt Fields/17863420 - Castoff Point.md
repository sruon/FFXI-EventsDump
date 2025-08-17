# 17863420 - Castoff Point

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Morimar Basalt Fields (ID: 265) |
| Block Size       | 592 bytes                       |
| Total Events     | 3                               |
| References Count | 28                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [18](#event-18)       | 0x0001       |    174 |             30 |
| [2588](#event-2588)   | 0x00AF       |    277 |             29 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0877      |        2167 |
|       2 | 0x089D      |        2205 |
|       3 | 0x1EC6      |        7878 |
|       4 | 0x1EC9      |        7881 |
|       5 | 0x0000      |           0 |
|       6 | 0x0004      |           4 |
|       7 | 0x00C8      |         200 |
|       8 | 0xFFF91C0B  |  4294515723 |
|       9 | 0x41878     |      268408 |
|      10 | 0xFFFF44C1  |  4294919361 |
|      11 | 0x0E00      |        3584 |
|      12 | 0xFFF8E4D8  |  4294501592 |
|      13 | 0x3E468     |      255080 |
|      14 | 0xFFFF44F7  |  4294919415 |
|      15 | 0x0600      |        1536 |
|      16 | 0xFFFF38EE  |  4294916334 |
|      17 | 0x29EEF     |      171759 |
|      18 | 0x063E      |        1598 |
|      19 | 0x0A2A      |        2602 |
|      20 | 0x0013      |          19 |
|      21 | 0xFFF8E9F1  |  4294502897 |
|      22 | 0x3E7BF     |      255935 |
|      23 | 0xFFFF4494  |  4294919316 |
|      24 | 0xFFFFFDA8  |  4294966696 |
|      25 | 0x0017      |          23 |
|      26 | 0x001E      |          30 |
|      27 | 0x005A      |          90 |

## String References

- **7878**: You should be able to head [to the other side/over there] if you have the $3 and $3.
- **7881**: Head [for the other side/over there]? [Yes./No./Dive right in.]

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
| Data Size    | 174 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 04 10 00 80 03 06  10 01 80 03 05 10 02 80   ...............
0010: 48 03 80 23 03 04 10 00  80 24 04 80 05 80 06 80  H..#.....$......
0020: 25 02 00 10 05 80 00 A2  00 42 43 00 43 01 1A B9  %........BC.C...
0030: 00 45 07 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0040: 05 80 55 07 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
0050: 31 02 02 10 05 80 80 68  00 47 00 08 80 09 80 0A  1......h.G......
0060: 80 0B 80 47 01 01 7F 00  02 02 10 00 80 80 7F 00  ...G............
0070: 47 00 0C 80 0D 80 0E 80  0F 80 47 01 01 7F 00 45  G.........G....E
0080: 07 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 05 80  ..........fdi1..
0090: 55 07 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  U..........fdi1.
00A0: AD 00 02 00 10 00 80 00  AD 00 01 AD 00 21 00     .............!. 
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[4] = 1*
  1: 0x0006 [0x03] Work_Zone[6] = 2167*
  2: 0x000B [0x03] Work_Zone[5] = 2205*
  3: 0x0010 [0x48] [System] [7878*]:
    → "You should be able to head [to the other side/over there] if you have the $3 and $3."
  4: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0014 [0x03] Work_Zone[4] = 1*
  6: 0x0019 [0x24] CREATE_DIALOG(message_id=7881*, default_option=0*, option_flags=4*)
    → "Head [for the other side/over there]? [Yes./No./Dive right in.]"
  7: 0x0020 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0021 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00A2
  9: 0x0029 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x002A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 11: 0x002C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 12: 0x002E [0x1A] CALL_SUBROUTINE(address=0x00B9)
 13: 0x0031 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0042 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 15: 0x0051 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0068
 16: 0x0059 [0x47] UPDATE_PLAYER_POS(-451.573*, 268.408*, -47.935*, yaw=315.0°*)
 17: 0x0063 [0x47] WAIT_PLAYER_POS_UPDATE
 18: 0x0065 [0x01] GOTO 0x007F
 19: 0x0068 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x007F
 20: 0x0070 [0x47] UPDATE_PLAYER_POS(-465.704*, 255.080*, -47.881*, yaw=135.0°*)
 21: 0x007A [0x47] WAIT_PLAYER_POS_UPDATE
 22: 0x007C [0x01] GOTO 0x007F

SUBROUTINE_007F:
 23: 0x007F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x0090 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 25: 0x009F [0x01] GOTO 0x00AD
 26: 0x00A2 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00AD
 27: 0x00AA [0x01] GOTO 0x00AD

SUBROUTINE_00AD:
 28: 0x00AD [0x21] END_EVENT
 29: 0x00AE [0x00] END_REQSTACK()
```

### Event 2588

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00AF    |
| Data Size    | 277 bytes |
| Instructions | 2         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               37                 7
00B0: 10 80 11 80 12 80 13 80  00 45 07 80 F0 FF FF 7F  .........E......
00C0: F0 FF FF 7F 66 64 6F 31  05 80 55 07 80 F0 FF FF  ....fdo1..U.....
00D0: 7F F0 FF FF 7F 66 64 6F  31 46 01 38 14 80 BA F0  .....fdo1F.8....
00E0: FF FF 7F 15 80 16 80 17  80 18 80 45 19 80 F0 FF  ...........E....
00F0: FF 7F F0 FF FF 7F 73 31  30 33 05 80 45 07 80 F0  ......s103..E...
0100: FF FF 7F F0 FF FF 7F 66  64 69 32 05 80 1C 1A 80  .......fdi2.....
0110: 27 10 F0 FF FF 7F 04 1C  1B 80 45 07 80 F0 FF FF  '.........E.....
0120: 7F F0 FF FF 7F 66 64 6F  31 05 80 55 07 80 F0 FF  .....fdo1..U....
0130: FF 7F F0 FF FF 7F 66 64  6F 31 2A 10 F0 FF FF 7F  ......fdo1*.....
0140: 29 10 FE 92 10 01 02 52  19 80 F0 FF FF 7F F0 FF  )......R........
0150: FF 7F 73 31 30 33 45 19  80 F0 FF FF 7F F0 FF FF  ..s103E.........
0160: 7F 73 31 30 34 05 80 45  07 80 F0 FF FF 7F F0 FF  .s104..E........
0170: FF 7F 66 64 69 32 05 80  1C 1A 80 27 10 F0 FF FF  ..fdi2.....'....
0180: 7F 05 1C 1B 80 45 07 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0190: 66 64 6F 31 05 80 55 07  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
01A0: 7F 66 64 6F 31 2A 10 F0  FF FF 7F 52 19 80 F0 FF  .fdo1*.....R....
01B0: FF 7F F0 FF FF 7F 73 31  30 34 29 10 FE 92 10 01  ......s104).....
01C0: 03 46 00 1B                                       .F..            
```

#### Opcodes

```
  0: 0x00AF [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-50.962*, z=171.759*, y=1.598*, direction=228.7°*
  1: 0x00B8 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x00CA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x00D9 [0x46] CAMERA_CONTROL: Disable user control
     0x00DB [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
     0x00DE [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-464.399*, pos_z=255.935*, pos_y=-47.980*, direction=377476166.5°*)
     0x00EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s103" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
     0x00FC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x010D [0x1C] WAIT(30* ticks)
     0x0110 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x04)
     0x0117 [0x1C] WAIT(90* ticks)
     0x011A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x012B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x013A [0x2A] GET_REQ_LEVEL(level=16, entity_id=LocalPlayer)
     0x0140 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Unnamed NPC (ID: 17863422/0x011092FE), tag_num=0x02)
     0x0147 [0x52] END_LOAD_SCHEDULER: End scheduler "s103" with entities [LocalPlayer, LocalPlayer], work=23*
     0x0156 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s104" with entities [LocalPlayer, LocalPlayer], work=[23*, 0*]
     0x0167 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0178 [0x1C] WAIT(30* ticks)
     0x017B [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x05)
     0x0182 [0x1C] WAIT(90* ticks)
     0x0185 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0196 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x01A5 [0x2A] GET_REQ_LEVEL(level=16, entity_id=LocalPlayer)
     0x01AB [0x52] END_LOAD_SCHEDULER: End scheduler "s104" with entities [LocalPlayer, LocalPlayer], work=23*
     0x01BA [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Unnamed NPC (ID: 17863422/0x011092FE), tag_num=0x03)
     0x01C1 [0x46] CAMERA_CONTROL: Restore default settings
     0x01C3 [0x1B] RETURN
```
