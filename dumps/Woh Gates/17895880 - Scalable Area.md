# 17895880 - Scalable Area

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Woh Gates (ID: 273) |
| Block Size       | 464 bytes           |
| Total Events     | 3                   |
| References Count | 22                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [201](#event-201)     | 0x0001       |    218 |             39 |
| [5504](#event-5504)   | 0x00DB       |    128 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x095F      |        2399 |
|       1 | 0x0954      |        2388 |
|       2 | 0x1E0C      |        7692 |
|       3 | 0x1E0D      |        7693 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x00C8      |         200 |
|       7 | 0x0013      |          19 |
|       8 | 0x378AD     |      227501 |
|       9 | 0xFFFFC529  |  4294952233 |
|      10 | 0x9BA3      |       39843 |
|      11 | 0x0002      |           2 |
|      12 | 0x36041     |      221249 |
|      13 | 0xFFFFC650  |  4294952528 |
|      14 | 0x74E9      |       29929 |
|      15 | 0xFFFFF830  |  4294965296 |
|      16 | 0x001E      |          30 |
|      17 | 0x000F      |          15 |
|      18 | 0x40000000  |  1073741824 |
|      19 | 0x005A      |          90 |
|      20 | 0x00C9      |         201 |
|      21 | 0x002D      |          45 |

## String References

- **7692**: You might be able to [descend/ascend] using these vines if you only had $3 and $6.
- **7693**: [Descend/Ascend]? [Yes./No.]

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

### Event 201

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 218 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 05 10 00 80 03 06  10 01 80 48 02 80 23 24   ..........H..#$
0010: 03 80 04 80 04 80 25 02  00 10 04 80 00 C9 00 42  ......%........B
0020: 03 01 10 05 80 43 00 43  01 4A F0 FF FF 7F F8 FF  .....C.C.J......
0030: FF 7F 6F 76 F0 FF FF 7F  45 06 80 F0 FF FF 7F F0  ..ov....E.......
0040: FF FF 7F 66 64 6F 31 04  80 55 06 80 F0 FF FF 7F  ...fdo1..U......
0050: F0 FF FF 7F 66 64 6F 31  38 07 80 02 07 10 05 80  ....fdo18.......
0060: 80 7F 00 BA F0 FF FF 7F  08 80 09 80 0A 80 04 80  ................
0070: 47 00 08 80 09 80 0A 80  04 80 47 01 01 A3 00 02  G.........G.....
0080: 07 10 0B 80 80 A3 00 BA  F0 FF FF 7F 0C 80 0D 80  ................
0090: 0E 80 0F 80 47 00 0C 80  0D 80 0E 80 0F 80 47 01  ....G.........G.
00A0: 01 A3 00 1C 10 80 80 F0  FF FF 7F 1C 11 80 AB 11  ................
00B0: 04 80 1C 05 80 45 06 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
00C0: 66 64 69 32 04 80 01 D9  00 02 00 10 05 80 00 D9  fdi2............
00D0: 00 03 01 10 12 80 01 D9  00 21 00                 .........!.     
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[5] = 2399*
  1: 0x0006 [0x03] Work_Zone[6] = 2388*
  2: 0x000B [0x48] [System] [7692*]:
    → "You might be able to [descend/ascend] using these vines if you only had $3 and $6."
  3: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000F [0x24] CREATE_DIALOG(message_id=7693*, default_option=0*, option_flags=0*)
    → "[Descend/Ascend]? [Yes./No.]"
  5: 0x0016 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0017 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C9
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
 18: 0x0063 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=227.501*, pos_z=-15.063*, pos_y=39.843*, direction=0.0°*)
 19: 0x0070 [0x47] UPDATE_PLAYER_POS(227.501*, -15.063*, 39.843*, yaw=0.0°*)
 20: 0x007A [0x47] WAIT_PLAYER_POS_UPDATE
 21: 0x007C [0x01] GOTO 0x00A3
 22: 0x007F [0x02] IF !(Work_Zone[7] == 2*) GOTO 0x00A3
 23: 0x0087 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=221.249*, pos_z=-14.768*, pos_y=29.929*, direction=377476043.4°*)
 24: 0x0094 [0x47] UPDATE_PLAYER_POS(221.249*, -14.768*, 29.929*, yaw=377476043.4°*)
 25: 0x009E [0x47] WAIT_PLAYER_POS_UPDATE
 26: 0x00A0 [0x01] GOTO 0x00A3

SUBROUTINE_00A3:
 27: 0x00A3 [0x1C] WAIT(30* ticks)
 28: 0x00A6 [0x80] LOAD_WAIT(entity=LocalPlayer)
 29: 0x00AB [0x1C] WAIT(15* ticks)
 30: 0x00AE [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
 31: 0x00B2 [0x1C] WAIT(1* ticks)
 32: 0x00B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 33: 0x00C6 [0x01] GOTO 0x00D9
 34: 0x00C9 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00D9
 35: 0x00D1 [0x03] Work_Zone[1] = 1073741824*
 36: 0x00D6 [0x01] GOTO 0x00D9

SUBROUTINE_00D9:
 37: 0x00D9 [0x21] END_EVENT
 38: 0x00DA [0x00] END_REQSTACK()
```

### Event 5504

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DB    |
| Data Size    | 128 bytes |
| Instructions | 14        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   42 45 06 80 F0             BE...
00E0: FF FF 7F F0 FF FF 7F 66  64 6F 31 04 80 62 05 80  .......fdo1..b..
00F0: F0 FF FF 7F F0 FF FF 7F  6D 61 69 6E 04 80 1C 13  ........main....
0100: 80 45 14 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 31  .E..........who1
0110: 04 80 55 14 80 F0 FF FF  7F F0 FF FF 7F 77 68 6F  ..U..........who
0120: 31 1C 15 80 45 06 80 F0  FF FF 7F F0 FF FF 7F 66  1...E..........f
0130: 64 6F 31 04 80 55 06 80  F0 FF FF 7F F0 FF FF 7F  do1..U..........
0140: 66 64 6F 31 45 14 80 F0  FF FF 7F F0 FF FF 7F 77  fdo1E..........w
0150: 68 69 31 04 80 1C 11 80  30 21 00                 hi1.....0!.     
```

#### Opcodes

```
  0: 0x00DB [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x00ED [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  3: 0x00FE [0x1C] WAIT(90* ticks)
  4: 0x0101 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0112 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
  6: 0x0121 [0x1C] WAIT(45* ticks)
  7: 0x0124 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0135 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  9: 0x0144 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x0155 [0x1C] WAIT(15* ticks)
 11: 0x0158 [0x30] SET_UCOFF_CONTINUE_ZERO()
 12: 0x0159 [0x21] END_EVENT
 13: 0x015A [0x00] END_REQSTACK()
```
