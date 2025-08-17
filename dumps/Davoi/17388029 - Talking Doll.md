# 17388029 - Talking Doll

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Davoi (ID: 149) |
| Block Size       | 2812 bytes      |
| Total Events     | 9               |
| References Count | 62              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [116](#event-116)        | 0x0001       |    536 |             71 |
| [65535.1](#event-655351) | 0x0219       |     10 |              2 |
| [65535.2](#event-655352) | 0x0223       |     10 |              2 |
| [65535.3](#event-655353) | 0x022D       |     10 |              2 |
| [65535.4](#event-655354) | 0x0237       |     10 |              2 |
| [124](#event-124)        | 0x0241       |     48 |             15 |
| [118](#event-118)        | 0x0271       |      1 |              1 |
| [126](#event-126)        | 0x0272       |   1885 |            245 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x00C8      |         200 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x007F      |         127 |
|       5 | 0x0001      |           1 |
|       6 | 0x0031      |          49 |
|       7 | 0x0DA5      |        3493 |
|       8 | 0x1D56      |        7510 |
|       9 | 0x0032      |          50 |
|      10 | 0x1D59      |        7513 |
|      11 | 0x0046      |          70 |
|      12 | 0x001E      |          30 |
|      13 | 0x0064      |         100 |
|      14 | 0x03E7      |         999 |
|      15 | 0xFFFE6A49  |  4294863433 |
|      16 | 0xFFFFF1C0  |  4294963648 |
|      17 | 0x03DE      |         990 |
|      18 | 0x0E05      |        3589 |
|      19 | 0xFFFE6B2C  |  4294863660 |
|      20 | 0xFFFFFF06  |  4294967046 |
|      21 | 0x0D33      |        3379 |
|      22 | 0xFFFFF67A  |  4294964858 |
|      23 | 0xFFFE5F77  |  4294860663 |
|      24 | 0x0478      |        1144 |
|      25 | 0xFFFFF940  |  4294965568 |
|      26 | 0xFFFE6BA0  |  4294863776 |
|      27 | 0x03A2      |         930 |
|      28 | 0x1D86      |        7558 |
|      29 | 0x1D8A      |        7562 |
|      30 | 0x0078      |         120 |
|      31 | 0x0018      |          24 |
|      32 | 0x00E7      |         231 |
|      33 | 0x1F08      |        7944 |
|      34 | 0x1F09      |        7945 |
|      35 | 0x0005      |           5 |
|      36 | 0x0006      |           6 |
|      37 | 0x1F0A      |        7946 |
|      38 | 0x1F0B      |        7947 |
|      39 | 0x1F0C      |        7948 |
|      40 | 0x1F0D      |        7949 |
|      41 | 0x1F0E      |        7950 |
|      42 | 0x1F0F      |        7951 |
|      43 | 0x1F10      |        7952 |
|      44 | 0x1F11      |        7953 |
|      45 | 0x1F12      |        7954 |
|      46 | 0x1F13      |        7955 |
|      47 | 0x1F14      |        7956 |
|      48 | 0x00A7      |         167 |
|      49 | 0x000C      |          12 |
|      50 | 0x005A      |          90 |
|      51 | 0x1F15      |        7957 |
|      52 | 0x1F16      |        7958 |
|      53 | 0x1F17      |        7959 |
|      54 | 0x0095      |         149 |
|      55 | 0x1F18      |        7960 |
|      56 | 0x1F19      |        7961 |
|      57 | 0x1F1A      |        7962 |
|      58 | 0x1F1B      |        7963 |
|      59 | 0x0E5A      |        3674 |
|      60 | 0x1F1C      |        7964 |
|      61 | 0x1F1D      |        7965 |

## String References

- **7558**: The $0 jumps in your hands.
- **7562**: Ahahahahaha! You're almost on top of it! It's somewhere in this area!

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

### Event 116

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 536 bytes |
| Instructions | 71        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 46 01 5D 00 80 01  80 1C 02 80 38 03 80 4E   BF.].......8..N
0010: 00 FE 51 09 01 4E 00 FF  51 09 01 80 FE 51 09 01  ..Q..N..Q....Q..
0020: 80 FF 51 09 01 29 08 F0  FF FF 7F 11 5C 00 04 80  ..Q..)......\...
0030: 5C 01 04 80 5D 04 80 05  80 1C 01 80 4E 01 F0 FF  \...].......N...
0040: FF 7F 29 0B FE 51 09 01  1C 29 0B FF 51 09 01 15  ..)..Q...)..Q...
0050: 27 0B FE 51 09 01 1D 45  06 80 F8 FF FF 7F F8 FF  '..Q...E........
0060: FF 7F 73 30 32 35 00 80  45 01 80 F8 FF FF 7F F8  ..s025..E.......
0070: FF FF 7F 66 64 69 31 00  80 1C 01 80 52 06 80 F8  ...fdi1.....R...
0080: FF FF 7F F8 FF FF 7F 73  30 32 35 45 01 80 F0 FF  .......s025E....
0090: FF 7F F0 FF FF 7F 6F 76  6C 31 00 80 45 06 80 F8  ......ovl1..E...
00A0: FF FF 7F F8 FF FF 7F 73  30 32 37 00 80 29 0B FF  .......s027..)..
00B0: 51 09 01 18 2A 0B FE 51  09 01 52 06 80 F8 FF FF  Q...*..Q..R.....
00C0: 7F F8 FF FF 7F 73 30 32  37 45 06 80 F8 FF FF 7F  .....s027E......
00D0: F8 FF FF 7F 73 30 32 36  00 80 79 00 FF 51 09 01  ....s026..y..Q..
00E0: FE 51 09 01 79 00 FE 51  09 01 FF 51 09 01 4B FE  .Q..y..Q...Q..K.
00F0: 51 09 01 07 80 29 0B FE  51 09 01 1F 27 0B FF 51  Q....)..Q...'..Q
0100: 09 01 16 2B FF 51 09 01  08 80 23 2A 0B FF 51 09  ...+.Q....#*..Q.
0110: 01 52 06 80 F8 FF FF 7F  F8 FF FF 7F 73 30 32 36  .R..........s026
0120: 45 06 80 F8 FF FF 7F F8  FF FF 7F 73 30 32 38 00  E..........s028.
0130: 80 4A FE 51 09 01 FF 51  09 01 6F 76 FE 51 09 01  .J.Q...Q..ov.Q..
0140: 1C 09 80 29 0B FE 51 09  01 20 29 0B FE 51 09 01  ...)..Q.. )..Q..
0150: 21 52 06 80 F8 FF FF 7F  F8 FF FF 7F 73 30 32 38  !R..........s028
0160: 45 06 80 F8 FF FF 7F F8  FF FF 7F 73 30 33 30 00  E..........s030.
0170: 80 79 00 FE 51 09 01 FF  51 09 01 2B FF 51 09 01  .y..Q...Q..+.Q..
0180: 0A 80 23 79 00 FE 51 09  01 F0 FF FF 7F 1C 0B 80  ..#y..Q.........
0190: 52 06 80 F8 FF FF 7F F8  FF FF 7F 73 30 33 30 45  R..........s030E
01A0: 01 80 F0 FF FF 7F F0 FF  FF 7F 6F 76 6C 31 00 80  ..........ovl1..
01B0: 45 06 80 F8 FF FF 7F F8  FF FF 7F 73 30 32 39 00  E..........s029.
01C0: 80 1C 0C 80 29 0B FE 51  09 01 22 5D 00 80 01 80  ....)..Q.."]....
01D0: 1C 0D 80 45 01 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
01E0: 6F 31 00 80 1C 01 80 4E  00 F0 FF FF 7F 80 F0 FF  o1.....N........
01F0: FF 7F 5C 00 00 80 5C 01  00 80 5D 04 80 05 80 46  ..\...\...]....F
0200: 00 1C 01 80 45 01 80 F8  FF FF 7F F8 FF FF 7F 66  ....E..........f
0210: 64 69 31 00 80 20 00 21  00                       di1.. .!.       
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0004 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
  3: 0x0009 [0x1C] WAIT(60* ticks)
  4: 0x000C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  5: 0x000F [0x4E] SET_ENTITY_HIDE_FLAG: Show Rochefogne (ID: 17388030/0x010951FE)
  6: 0x0015 [0x4E] SET_ENTITY_HIDE_FLAG: Show Vauderame (ID: 17388031/0x010951FF)
  7: 0x001B [0x80] LOAD_WAIT(entity=Rochefogne (ID: 17388030/0x010951FE))
  8: 0x0020 [0x80] LOAD_WAIT(entity=Vauderame (ID: 17388031/0x010951FF))
  9: 0x0025 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x11)
 10: 0x002C [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 127*
 11: 0x0030 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 127*
 12: 0x0034 [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
 13: 0x0039 [0x1C] WAIT(200* ticks)
 14: 0x003C [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
 15: 0x0042 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rochefogne (ID: 17388030/0x010951FE), tag_num=0x1C)
 16: 0x0049 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17388031/0x010951FF), tag_num=0x15)
 17: 0x0050 [0x27] REQ_SET(priority=0x0B, entity_id=Rochefogne (ID: 17388030/0x010951FE), tag_num=0x1D)
 18: 0x0057 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s025" with entities [EventEntity, EventEntity], work=[49*, 0*]
 19: 0x0068 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 20: 0x0079 [0x1C] WAIT(200* ticks)
 21: 0x007C [0x52] END_LOAD_SCHEDULER: End scheduler "s025" with entities [EventEntity, EventEntity], work=49*
 22: 0x008B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x009C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s027" with entities [EventEntity, EventEntity], work=[49*, 0*]
 24: 0x00AD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vauderame (ID: 17388031/0x010951FF), tag_num=0x18)
 25: 0x00B4 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Rochefogne (ID: 17388030/0x010951FE))
 26: 0x00BA [0x52] END_LOAD_SCHEDULER: End scheduler "s027" with entities [EventEntity, EventEntity], work=49*
 27: 0x00C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s026" with entities [EventEntity, EventEntity], work=[49*, 0*]
 28: 0x00DA [0x79] Vauderame (ID: 17388031/0x010951FF) looks at Rochefogne (ID: 17388030/0x010951FE) (Basic look)
 29: 0x00E4 [0x79] Rochefogne (ID: 17388030/0x010951FE) looks at Vauderame (ID: 17388031/0x010951FF) (Basic look)
 30: 0x00EE [0x4B] UPDATE_ENTITY_YAW(entity=Rochefogne (ID: 17388030/0x010951FE), yaw=19.2°*)
 31: 0x00F5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rochefogne (ID: 17388030/0x010951FE), tag_num=0x1F)
 32: 0x00FC [0x27] REQ_SET(priority=0x0B, entity_id=Vauderame (ID: 17388031/0x010951FF), tag_num=0x16)
 33: 0x0103 [0x2B] Vauderame (ID: 17388031/0x010951FF) [7510*]:
    → "Well, no matter. The fact is, there is someone else who is looking for the sword. And, either they have got to it first or..."
 34: 0x010A [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x010B [0x2A] GET_REQ_LEVEL(level=11, entity_id=Vauderame (ID: 17388031/0x010951FF))
 36: 0x0111 [0x52] END_LOAD_SCHEDULER: End scheduler "s026" with entities [EventEntity, EventEntity], work=49*
 37: 0x0120 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s028" with entities [EventEntity, EventEntity], work=[49*, 0*]
 38: 0x0131 [0x4A] Rochefogne (ID: 17388030/0x010951FE) looks at Vauderame (ID: 17388031/0x010951FF)
 39: 0x013A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 40: 0x013B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Rochefogne (ID: 17388030/0x010951FE) Render.Flags0 and Render.Flags3 conditions are met
 41: 0x0140 [0x1C] WAIT(50* ticks)
 42: 0x0143 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rochefogne (ID: 17388030/0x010951FE), tag_num=0x20)
 43: 0x014A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rochefogne (ID: 17388030/0x010951FE), tag_num=0x21)
 44: 0x0151 [0x52] END_LOAD_SCHEDULER: End scheduler "s028" with entities [EventEntity, EventEntity], work=49*
 45: 0x0160 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s030" with entities [EventEntity, EventEntity], work=[49*, 0*]
 46: 0x0171 [0x79] Rochefogne (ID: 17388030/0x010951FE) looks at Vauderame (ID: 17388031/0x010951FF) (Basic look)
 47: 0x017B [0x2B] Vauderame (ID: 17388031/0x010951FF) [7513*]:
    → "...nuisance..."
 48: 0x0182 [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x0183 [0x79] Rochefogne (ID: 17388030/0x010951FE) looks at LocalPlayer (Basic look)
 50: 0x018D [0x1C] WAIT(70* ticks)
 51: 0x0190 [0x52] END_LOAD_SCHEDULER: End scheduler "s030" with entities [EventEntity, EventEntity], work=49*
 52: 0x019F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 53: 0x01B0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s029" with entities [EventEntity, EventEntity], work=[49*, 0*]
 54: 0x01C1 [0x1C] WAIT(30* ticks)
 55: 0x01C4 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Rochefogne (ID: 17388030/0x010951FE), tag_num=0x22)
 56: 0x01CB [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=200*)
 57: 0x01D0 [0x1C] WAIT(100* ticks)
 58: 0x01D3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 59: 0x01E4 [0x1C] WAIT(200* ticks)
 60: 0x01E7 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 61: 0x01ED [0x80] LOAD_WAIT(entity=LocalPlayer)
 62: 0x01F2 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 63: 0x01F6 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 64: 0x01FA [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=1*)
 65: 0x01FF [0x46] CAMERA_CONTROL: Restore default settings
 66: 0x0201 [0x1C] WAIT(200* ticks)
 67: 0x0204 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 68: 0x0215 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 69: 0x0217 [0x21] END_EVENT
 70: 0x0218 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0219   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                             37 0E 80 0F 80 10 80           7......
0220: 11 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0219 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.999*, z=-103.863*, y=-3.648*, direction=87.0°*
  1: 0x0222 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0223   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:          37 12 80 13 80  14 80 15 80 00              7.........   
```

#### Opcodes

```
  0: 0x0223 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=3.589*, z=-103.636*, y=-0.250*, direction=297.0°*
  1: 0x022C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                         37 16 80               7..
0230: 17 80 14 80 18 80 00                              .......         
```

#### Opcodes

```
  0: 0x022D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.438*, z=-106.633*, y=-0.250*, direction=100.5°*
  1: 0x0236 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0237   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                      37  19 80 1A 80 14 80 1B 80         7........
0240: 00                                                .               
```

#### Opcodes

```
  0: 0x0237 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-1.728*, z=-103.520*, y=-0.250*, direction=81.7°*
  1: 0x0240 [0x00] END_REQSTACK()
```

### Event 124

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0241   |
| Data Size    | 48 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:    42 1C 05 80 43 00 43  01 1C 05 80 48 1C 80 23   B...C.C....H..#
0250: 1D 1D 80 23 4E 00 F0 FF  FF 7F 46 00 45 01 80 F8  ...#N.....F.E...
0260: FF FF 7F F8 FF FF 7F 66  64 69 31 00 80 20 00 21  .......fdi1.. .!
0270: 00                                                .               
```

#### Opcodes

```
  0: 0x0241 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0242 [0x1C] WAIT(1* ticks)
  2: 0x0245 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0247 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x0249 [0x1C] WAIT(1* ticks)
  5: 0x024C [0x48] [System] [7558*]:
    → "The $0 jumps in your hands."
  6: 0x024F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0250 [0x1D] PRINT_EVENT_MESSAGE(message_id=7562*)
    → "Ahahahahaha! You're almost on top of it! It's somewhere in this area!"
  8: 0x0253 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0254 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 10: 0x025A [0x46] CAMERA_CONTROL: Restore default settings
 11: 0x025C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 12: 0x026D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x026F [0x21] END_EVENT
 14: 0x0270 [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0271  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:    00                                              .              
```

#### Opcodes

```
  0: 0x0271 [0x00] END_REQSTACK()
```

### Event 126

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0272     |
| Data Size    | 1885 bytes |
| Instructions | 245        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:       20 01 42 46 01 5D  00 80 1E 80 45 01 80 F8     .BF.]....E...
0280: FF FF 7F F8 FF FF 7F 66  64 6F 31 00 80 1C 1E 80  .......fdo1.....
0290: 38 03 80 29 08 F0 FF FF  7F 11 29 0B 01 52 09 01  8..)......)..R..
02A0: 20 29 0B F0 FF FF 7F 15  4E 00 01 52 09 01 80 01   )......N..R....
02B0: 52 09 01 92 01 01 52 09  01 27 0B 01 52 09 01 21  R.....R..'..R..!
02C0: 45 1F 80 F8 FF FF 7F F8  FF FF 7F 73 30 35 34 00  E..........s054.
02D0: 80 45 01 80 F8 FF FF 7F  F8 FF FF 7F 66 64 69 31  .E..........fdi1
02E0: 00 80 1C 02 80 5C 00 20  80 5C 01 20 80 4A F0 FF  .....\. .\. .J..
02F0: FF 7F 01 52 09 01 6F 76  F0 FF FF 7F 02 08 10 00  ...R..ov........
0300: 80 00 0F 03 2B 01 52 09  01 21 80 23 01 17 03 2B  ....+.R..!.#...+
0310: 01 52 09 01 22 80 23 2A  0B 01 52 09 01 45 01 80  .R..".#*..R..E..
0320: F8 FF FF 7F F8 FF FF 7F  66 64 6F 31 00 80 1C 02  ........fdo1....
0330: 80 52 1F 80 F8 FF FF 7F  F8 FF FF 7F 73 30 35 34  .R..........s054
0340: 29 08 01 52 09 01 05 29  08 01 52 09 01 06 7B 01  )..R...)..R...{.
0350: 52 09 01 02 09 10 23 80  00 6F 03 45 1F 80 F8 FF  R.....#..o.E....
0360: FF 7F F8 FF FF 7F 73 30  36 33 00 80 01 9C 03 02  ......s063......
0370: 09 10 24 80 00 8B 03 45  1F 80 F8 FF FF 7F F8 FF  ..$....E........
0380: FF 7F 73 30 36 33 00 80  01 9C 03 45 1F 80 F8 FF  ..s063.....E....
0390: FF 7F F8 FF FF 7F 73 30  35 35 00 80 45 01 80 F8  ......s055..E...
03A0: FF FF 7F F8 FF FF 7F 66  64 69 31 00 80 2B 01 52  .......fdi1..+.R
03B0: 09 01 25 80 23 2B 01 52  09 01 26 80 23 02 09 10  ..%.#+.R..&.#...
03C0: 23 80 00 D7 03 52 1F 80  F8 FF FF 7F F8 FF FF 7F  #....R..........
03D0: 73 30 36 33 01 00 04 02  09 10 24 80 00 F1 03 52  s063......$....R
03E0: 1F 80 F8 FF FF 7F F8 FF  FF 7F 73 30 36 33 01 00  ..........s063..
03F0: 04 52 1F 80 F8 FF FF 7F  F8 FF FF 7F 73 30 35 35  .R..........s055
0400: 45 1F 80 F8 FF FF 7F F8  FF FF 7F 73 30 35 36 00  E..........s056.
0410: 80 29 08 01 52 09 01 07  02 08 10 00 80 00 2B 04  .)..R.........+.
0420: 2B 01 52 09 01 27 80 23  01 33 04 2B 01 52 09 01  +.R..'.#.3.+.R..
0430: 28 80 23 29 08 01 52 09  01 08 2B 01 52 09 01 29  (.#)..R...+.R..)
0440: 80 23 52 1F 80 F8 FF FF  7F F8 FF FF 7F 73 30 35  .#R..........s05
0450: 36 02 09 10 23 80 00 6D  04 45 1F 80 F8 FF FF 7F  6...#..m.E......
0460: F8 FF FF 7F 73 30 36 34  00 80 01 9A 04 02 09 10  ....s064........
0470: 24 80 00 89 04 45 1F 80  F8 FF FF 7F F8 FF FF 7F  $....E..........
0480: 73 30 36 34 00 80 01 9A  04 45 1F 80 F8 FF FF 7F  s064.....E......
0490: F8 FF FF 7F 73 30 35 37  00 80 27 0B 01 52 09 01  ....s057..'..R..
04A0: 22 2B 01 52 09 01 2A 80  23 2A 0B 01 52 09 01 02  "+.R..*.#*..R...
04B0: 09 10 23 80 00 C9 04 52  1F 80 F8 FF FF 7F F8 FF  ..#....R........
04C0: FF 7F 73 30 36 34 01 F2  04 02 09 10 24 80 00 E3  ..s064......$...
04D0: 04 52 1F 80 F8 FF FF 7F  F8 FF FF 7F 73 30 36 34  .R..........s064
04E0: 01 F2 04 52 1F 80 F8 FF  FF 7F F8 FF FF 7F 73 30  ...R..........s0
04F0: 35 37 45 01 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  57E..........ovl
0500: 31 00 80 45 1F 80 F8 FF  FF 7F F8 FF FF 7F 73 30  1..E..........s0
0510: 35 38 00 80 4A F0 FF FF  7F 01 52 09 01 29 08 01  58..J.....R..)..
0520: 52 09 01 15 2B 01 52 09  01 2B 80 23 29 08 01 52  R...+.R..+.#)..R
0530: 09 01 16 79 00 01 52 09  01 F0 FF FF 7F 29 08 01  ...y..R......)..
0540: 52 09 01 17 2B 01 52 09  01 2C 80 23 29 08 01 52  R...+.R..,.#)..R
0550: 09 01 18 6F 76 F0 FF FF  7F 52 1F 80 F8 FF FF 7F  ...ov....R......
0560: F8 FF FF 7F 73 30 35 38  02 09 10 23 80 00 84 05  ....s058...#....
0570: 45 1F 80 F8 FF FF 7F F8  FF FF 7F 73 30 36 35 00  E..........s065.
0580: 80 01 B1 05 02 09 10 24  80 00 A0 05 45 1F 80 F8  .......$....E...
0590: FF FF 7F F8 FF FF 7F 73  30 36 35 00 80 01 B1 05  .......s065.....
05A0: 45 1F 80 F8 FF FF 7F F8  FF FF 7F 73 30 35 39 00  E..........s059.
05B0: 80 4A 01 52 09 01 F0 FF  FF 7F 6F 76 01 52 09 01  .J.R......ov.R..
05C0: 2B 01 52 09 01 2D 80 23  2B 01 52 09 01 2E 80 23  +.R..-.#+.R....#
05D0: 02 09 10 23 80 00 EA 05  52 1F 80 F8 FF FF 7F F8  ...#....R.......
05E0: FF FF 7F 73 30 36 35 01  13 06 02 09 10 24 80 00  ...s065......$..
05F0: 04 06 52 1F 80 F8 FF FF  7F F8 FF FF 7F 73 30 36  ..R..........s06
0600: 35 01 13 06 52 1F 80 F8  FF FF 7F F8 FF FF 7F 73  5...R..........s
0610: 30 35 39 45 01 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  059E..........ov
0620: 6C 31 00 80 02 09 10 23  80 00 40 06 45 1F 80 F8  l1.....#..@.E...
0630: FF FF 7F F8 FF FF 7F 73  30 36 36 00 80 01 6D 06  .......s066...m.
0640: 02 09 10 24 80 00 5C 06  45 1F 80 F8 FF FF 7F F8  ...$..\.E.......
0650: FF FF 7F 73 30 36 36 00  80 01 6D 06 45 1F 80 F8  ...s066...m.E...
0660: FF FF 7F F8 FF FF 7F 73  30 36 30 00 80 2B 01 52  .......s060..+.R
0670: 09 01 2F 80 23 5D 00 80  1E 80 45 01 80 F8 FF FF  ../.#]....E.....
0680: 7F F8 FF FF 7F 66 64 6F  31 00 80 1C 1E 80 02 09  .....fdo1.......
0690: 10 23 80 00 A8 06 52 1F  80 F8 FF FF 7F F8 FF FF  .#....R.........
06A0: 7F 73 30 36 36 01 D1 06  02 09 10 24 80 00 C2 06  .s066......$....
06B0: 52 1F 80 F8 FF FF 7F F8  FF FF 7F 73 30 36 36 01  R..........s066.
06C0: D1 06 52 1F 80 F8 FF FF  7F F8 FF FF 7F 73 30 36  ..R..........s06
06D0: 30 34 30 80 77 31 80 05  80 1C 32 80 4E 01 F0 FF  040.w1....2.N...
06E0: FF 7F 4E 01 01 52 09 01  4E 00 02 52 09 01 4E 00  ..N..R..N..R..N.
06F0: 03 52 09 01 80 03 52 09  01 80 02 52 09 01 92 01  .R....R....R....
0700: 03 52 09 01 92 01 02 52  09 01 29 0B 03 52 09 01  .R.....R..)..R..
0710: 20 29 0B 02 52 09 01 20  29 08 02 52 09 01 1D 27   )..R.. )..R...'
0720: 0B 03 52 09 01 21 45 1F  80 F8 FF FF 7F F8 FF FF  ..R..!E.........
0730: 7F 73 30 36 37 00 80 45  01 80 F8 FF FF 7F F8 FF  .s067..E........
0740: FF 7F 66 64 69 31 00 80  1C 0D 80 2B 01 52 09 01  ..fdi1.....+.R..
0750: 33 80 23 52 1F 80 F8 FF  FF 7F F8 FF FF 7F 73 30  3.#R..........s0
0760: 36 37 45 01 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  67E..........ovl
0770: 31 00 80 45 1F 80 F8 FF  FF 7F F8 FF FF 7F 73 30  1..E..........s0
0780: 36 38 00 80 2B 01 52 09  01 34 80 23 2B 01 52 09  68..+.R..4.#+.R.
0790: 01 35 80 23 52 1F 80 F8  FF FF 7F F8 FF FF 7F 73  .5.#R..........s
07A0: 30 36 38 45 01 80 F8 FF  FF 7F F8 FF FF 7F 66 64  068E..........fd
07B0: 6F 31 00 80 1C 02 80 35  36 80 78 1C 32 80 29 0B  o1.....56.x.2.).
07C0: 01 52 09 01 23 29 0B F0  FF FF 7F 15 5D 04 80 1E  .R..#)......]...
07D0: 80 4E 00 F0 FF FF 7F 4E  00 01 52 09 01 80 F0 FF  .N.....N..R.....
07E0: FF 7F 80 01 52 09 01 4E  01 02 52 09 01 4E 01 03  ....R..N..R..N..
07F0: 52 09 01 4A F0 FF FF 7F  01 52 09 01 6F 76 F0 FF  R..J.....R..ov..
0800: FF 7F 02 09 10 23 80 00  1E 08 45 1F 80 F8 FF FF  .....#....E.....
0810: 7F F8 FF FF 7F 73 30 36  33 00 80 01 4B 08 02 09  .....s063...K...
0820: 10 24 80 00 3A 08 45 1F  80 F8 FF FF 7F F8 FF FF  .$..:.E.........
0830: 7F 73 30 36 33 00 80 01  4B 08 45 1F 80 F8 FF FF  .s063...K.E.....
0840: 7F F8 FF FF 7F 73 30 35  35 00 80 27 0B 01 52 09  .....s055..'..R.
0850: 01 24 45 01 80 F8 FF FF  7F F8 FF FF 7F 66 64 69  .$E..........fdi
0860: 31 00 80 2B 01 52 09 01  37 80 23 2B 01 52 09 01  1..+.R..7.#+.R..
0870: 38 80 23 2A 0B 01 52 09  01 02 09 10 23 80 00 93  8.#*..R.....#...
0880: 08 52 1F 80 F8 FF FF 7F  F8 FF FF 7F 73 30 36 33  .R..........s063
0890: 01 BC 08 02 09 10 24 80  00 AD 08 52 1F 80 F8 FF  ......$....R....
08A0: FF 7F F8 FF FF 7F 73 30  36 33 01 BC 08 52 1F 80  ......s063...R..
08B0: F8 FF FF 7F F8 FF FF 7F  73 30 35 35 45 1F 80 F8  ........s055E...
08C0: FF FF 7F F8 FF FF 7F 73  30 35 36 00 80 4A 01 52  .......s056..J.R
08D0: 09 01 F0 FF FF 7F 6F 76  01 52 09 01 29 08 01 52  ......ov.R..)..R
08E0: 09 01 01 2B 01 52 09 01  39 80 23 2B 01 52 09 01  ...+.R..9.#+.R..
08F0: 3A 80 23 29 08 01 52 09  01 02 52 1F 80 F8 FF FF  :.#)..R...R.....
0900: 7F F8 FF FF 7F 73 30 35  36 45 1F 80 F8 FF FF 7F  .....s056E......
0910: F8 FF FF 7F 73 30 36 31  00 80 7B 01 52 09 01 4B  ....s061..{.R..K
0920: 01 52 09 01 3B 80 6F 76  01 52 09 01 2B 01 52 09  .R..;.ov.R..+.R.
0930: 01 3C 80 23 2B 01 52 09  01 3D 80 23 52 1F 80 F8  .<.#+.R..=.#R...
0940: FF FF 7F F8 FF FF 7F 73  30 36 31 45 01 80 F0 FF  .......s061E....
0950: FF 7F F0 FF FF 7F 6F 76  6C 31 00 80 45 1F 80 F8  ......ovl1..E...
0960: FF FF 7F F8 FF FF 7F 73  30 36 32 00 80 27 0B 01  .......s062..'..
0970: 52 09 01 25 5D 00 80 1E  80 1C 32 80 45 01 80 F0  R..%].....2.E...
0980: FF FF 7F F0 FF FF 7F 66  64 6F 31 00 80 1C 1E 80  .......fdo1.....
0990: 2A 0B 01 52 09 01 52 1F  80 F8 FF FF 7F F8 FF FF  *..R..R.........
09A0: 7F 73 30 36 32 5C 00 00  80 5C 01 00 80 4E 00 F0  .s062\...\...N..
09B0: FF FF 7F 80 F0 FF FF 7F  46 00 45 01 80 F0 FF FF  ........F.E.....
09C0: 7F F0 FF FF 7F 66 64 69  31 00 80 20 00 21 00     .....fdi1.. .!. 
```

#### Opcodes

```
  0: 0x0272 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0274 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0275 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0277 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=120*)
  4: 0x027C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  5: 0x028D [0x1C] WAIT(120* ticks)
  6: 0x0290 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  7: 0x0293 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x11)
  8: 0x029A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x20)
  9: 0x02A1 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x15)
 10: 0x02A8 [0x4E] SET_ENTITY_HIDE_FLAG: Show Dauperiat (ID: 17388033/0x01095201)
 11: 0x02AE [0x80] LOAD_WAIT(entity=Dauperiat (ID: 17388033/0x01095201))
 12: 0x02B3 [0x92] Dauperiat (ID: 17388033/0x01095201)->Render.Flags3 ^= 0x01
 13: 0x02B9 [0x27] REQ_SET(priority=0x0B, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x21)
 14: 0x02C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s054" with entities [EventEntity, EventEntity], work=[24*, 0*]
 15: 0x02D1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 16: 0x02E2 [0x1C] WAIT(60* ticks)
 17: 0x02E5 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 231*
 18: 0x02E9 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 231*
 19: 0x02ED [0x4A] LocalPlayer looks at Dauperiat (ID: 17388033/0x01095201)
 20: 0x02F6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 21: 0x02F7 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 22: 0x02FC [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x030F
 23: 0x0304 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7944*]:
    → "Impressive... You don't look like one of Teulomme's lackeys. Who are you?"
 24: 0x030B [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x030C [0x01] GOTO 0x0317
 26: 0x030F [0x2B] Dauperiat (ID: 17388033/0x01095201) [7945*]:
    → "Impressive... You don't look like one of Teulomme's lackeys. Wait...you're that adventurer."
 27: 0x0316 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0317:
 28: 0x0317 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Dauperiat (ID: 17388033/0x01095201))
 29: 0x031D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 30: 0x032E [0x1C] WAIT(60* ticks)
 31: 0x0331 [0x52] END_LOAD_SCHEDULER: End scheduler "s054" with entities [EventEntity, EventEntity], work=24*
 32: 0x0340 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x05)
 33: 0x0347 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x06)
 34: 0x034E [0x7B] Dauperiat (ID: 17388033/0x01095201) stops talking
 35: 0x0353 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x036F
 36: 0x035B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s063" with entities [EventEntity, EventEntity], work=[24*, 0*]
 37: 0x036C [0x01] GOTO 0x039C
 38: 0x036F [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x038B
 39: 0x0377 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s063" with entities [EventEntity, EventEntity], work=[24*, 0*]
 40: 0x0388 [0x01] GOTO 0x039C
 41: 0x038B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s055" with entities [EventEntity, EventEntity], work=[24*, 0*]

SUBROUTINE_039C:
 42: 0x039C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 43: 0x03AD [0x2B] Dauperiat (ID: 17388033/0x01095201) [7946*]:
    → "Hrmph. So you heard someone was threatening the count, and you were asked to find out who it was?"
 44: 0x03B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x03B5 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7947*]:
    → "So now that you've found me, it's straight to the Royal Knights, I suppose?"
 46: 0x03BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x03BD [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x03D7
 48: 0x03C5 [0x52] END_LOAD_SCHEDULER: End scheduler "s063" with entities [EventEntity, EventEntity], work=24*
 49: 0x03D4 [0x01] GOTO 0x0400
 50: 0x03D7 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x03F1
 51: 0x03DF [0x52] END_LOAD_SCHEDULER: End scheduler "s063" with entities [EventEntity, EventEntity], work=24*
 52: 0x03EE [0x01] GOTO 0x0400
 53: 0x03F1 [0x52] END_LOAD_SCHEDULER: End scheduler "s055" with entities [EventEntity, EventEntity], work=24*

SUBROUTINE_0400:
 54: 0x0400 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s056" with entities [EventEntity, EventEntity], work=[24*, 0*]
 55: 0x0411 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x07)
 56: 0x0418 [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x042B
 57: 0x0420 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7948*]:
    → "No? What an unusual request you've undertaken."
 58: 0x0427 [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0428 [0x01] GOTO 0x0433
 60: 0x042B [0x2B] Dauperiat (ID: 17388033/0x01095201) [7949*]:
    → "No? You always were one for undertaking unusual requests."
 61: 0x0432 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0433:
 62: 0x0433 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x08)
 63: 0x043A [0x2B] Dauperiat (ID: 17388033/0x01095201) [7950*]:
    → "Very well. Seeing as you've brought me the $1, I should consider you a welcome guest. I'll let you in on a little secret about Count Teulomme."
 64: 0x0441 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x0442 [0x52] END_LOAD_SCHEDULER: End scheduler "s056" with entities [EventEntity, EventEntity], work=24*
 66: 0x0451 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x046D
 67: 0x0459 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s064" with entities [EventEntity, EventEntity], work=[24*, 0*]
 68: 0x046A [0x01] GOTO 0x049A
 69: 0x046D [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x0489
 70: 0x0475 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s064" with entities [EventEntity, EventEntity], work=[24*, 0*]
 71: 0x0486 [0x01] GOTO 0x049A
 72: 0x0489 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s057" with entities [EventEntity, EventEntity], work=[24*, 0*]

SUBROUTINE_049A:
 73: 0x049A [0x27] REQ_SET(priority=0x0B, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x22)
 74: 0x04A1 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7951*]:
    → "I assume you've heard of Atarefaunet's Band? Did you know their services could be bought for the right price?"
 75: 0x04A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 76: 0x04A9 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Dauperiat (ID: 17388033/0x01095201))
 77: 0x04AF [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x04C9
 78: 0x04B7 [0x52] END_LOAD_SCHEDULER: End scheduler "s064" with entities [EventEntity, EventEntity], work=24*
 79: 0x04C6 [0x01] GOTO 0x04F2
 80: 0x04C9 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x04E3
 81: 0x04D1 [0x52] END_LOAD_SCHEDULER: End scheduler "s064" with entities [EventEntity, EventEntity], work=24*
 82: 0x04E0 [0x01] GOTO 0x04F2
 83: 0x04E3 [0x52] END_LOAD_SCHEDULER: End scheduler "s057" with entities [EventEntity, EventEntity], work=24*

SUBROUTINE_04F2:
 84: 0x04F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 85: 0x0503 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s058" with entities [EventEntity, EventEntity], work=[24*, 0*]
 86: 0x0514 [0x4A] LocalPlayer looks at Dauperiat (ID: 17388033/0x01095201)
 87: 0x051D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x15)
 88: 0x0524 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7952*]:
    → "Even now, most people regard them as little more than a band of particularly vicious thieves."
 89: 0x052B [0x23] WAIT_FOR_DIALOG_INTERACTION
 90: 0x052C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x16)
 91: 0x0533 [0x79] Dauperiat (ID: 17388033/0x01095201) looks at LocalPlayer (Basic look)
 92: 0x053D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x17)
 93: 0x0544 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7953*]:
    → "A client utilizing their talents for unsavory deeds could thus escape any incrimination."
 94: 0x054B [0x23] WAIT_FOR_DIALOG_INTERACTION
 95: 0x054C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x18)
 96: 0x0553 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 97: 0x0554 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 98: 0x0559 [0x52] END_LOAD_SCHEDULER: End scheduler "s058" with entities [EventEntity, EventEntity], work=24*
 99: 0x0568 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x0584
100: 0x0570 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s065" with entities [EventEntity, EventEntity], work=[24*, 0*]
101: 0x0581 [0x01] GOTO 0x05B1
102: 0x0584 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x05A0
103: 0x058C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s065" with entities [EventEntity, EventEntity], work=[24*, 0*]
104: 0x059D [0x01] GOTO 0x05B1
105: 0x05A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s059" with entities [EventEntity, EventEntity], work=[24*, 0*]

SUBROUTINE_05B1:
106: 0x05B1 [0x4A] Dauperiat (ID: 17388033/0x01095201) looks at LocalPlayer
107: 0x05BA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
108: 0x05BB [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dauperiat (ID: 17388033/0x01095201) Render.Flags0 and Render.Flags3 conditions are met
109: 0x05C0 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7954*]:
    → "But after the war ended, the leader of the band, Atarefaunet, was captured by a pair of bounty hunters."
110: 0x05C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
111: 0x05C8 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7955*]:
    → "Naturally, the band's clients were falling over themselves to have him silenced before all their dirty secrets came to light."
112: 0x05CF [0x23] WAIT_FOR_DIALOG_INTERACTION
113: 0x05D0 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x05EA
114: 0x05D8 [0x52] END_LOAD_SCHEDULER: End scheduler "s065" with entities [EventEntity, EventEntity], work=24*
115: 0x05E7 [0x01] GOTO 0x0613
116: 0x05EA [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x0604
117: 0x05F2 [0x52] END_LOAD_SCHEDULER: End scheduler "s065" with entities [EventEntity, EventEntity], work=24*
118: 0x0601 [0x01] GOTO 0x0613
119: 0x0604 [0x52] END_LOAD_SCHEDULER: End scheduler "s059" with entities [EventEntity, EventEntity], work=24*

SUBROUTINE_0613:
120: 0x0613 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
121: 0x0624 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x0640
122: 0x062C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s066" with entities [EventEntity, EventEntity], work=[24*, 0*]
123: 0x063D [0x01] GOTO 0x066D
124: 0x0640 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x065C
125: 0x0648 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s066" with entities [EventEntity, EventEntity], work=[24*, 0*]
126: 0x0659 [0x01] GOTO 0x066D
127: 0x065C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s060" with entities [EventEntity, EventEntity], work=[24*, 0*]

SUBROUTINE_066D:
128: 0x066D [0x2B] Dauperiat (ID: 17388033/0x01095201) [7956*]:
    → "One of those clients was our very own Count Teulomme. The man who lords it over the territory of Carpenters' Landing."
129: 0x0674 [0x23] WAIT_FOR_DIALOG_INTERACTION
130: 0x0675 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=120*)
131: 0x067A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
132: 0x068B [0x1C] WAIT(120* ticks)
133: 0x068E [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x06A8
134: 0x0696 [0x52] END_LOAD_SCHEDULER: End scheduler "s066" with entities [EventEntity, EventEntity], work=24*
135: 0x06A5 [0x01] GOTO 0x06D1
136: 0x06A8 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x06C2
137: 0x06B0 [0x52] END_LOAD_SCHEDULER: End scheduler "s066" with entities [EventEntity, EventEntity], work=24*
138: 0x06BF [0x01] GOTO 0x06D1
139: 0x06C2 [0x52] END_LOAD_SCHEDULER: End scheduler "s060" with entities [EventEntity, EventEntity], work=24*

SUBROUTINE_06D1:
140: 0x06D1 [0x34] LOAD_UNLOAD_ZONE(zone_id=167*)
141: 0x06D4 [0x77] SET_EVENT_TIME_WEATHER(hour=12*, weather=1*)
142: 0x06D9 [0x1C] WAIT(90* ticks)
143: 0x06DC [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
144: 0x06E2 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Dauperiat (ID: 17388033/0x01095201)
145: 0x06E8 [0x4E] SET_ENTITY_HIDE_FLAG: Show Atarefaunet (ID: 17388034/0x01095202)
146: 0x06EE [0x4E] SET_ENTITY_HIDE_FLAG: Show Monban01 (ID: 17388035/0x01095203)
147: 0x06F4 [0x80] LOAD_WAIT(entity=Monban01 (ID: 17388035/0x01095203))
148: 0x06F9 [0x80] LOAD_WAIT(entity=Atarefaunet (ID: 17388034/0x01095202))
149: 0x06FE [0x92] Monban01 (ID: 17388035/0x01095203)->Render.Flags3 ^= 0x01
150: 0x0704 [0x92] Atarefaunet (ID: 17388034/0x01095202)->Render.Flags3 ^= 0x01
151: 0x070A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Monban01 (ID: 17388035/0x01095203), tag_num=0x20)
152: 0x0711 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Atarefaunet (ID: 17388034/0x01095202), tag_num=0x20)
153: 0x0718 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Atarefaunet (ID: 17388034/0x01095202), tag_num=0x1D)
154: 0x071F [0x27] REQ_SET(priority=0x0B, entity_id=Monban01 (ID: 17388035/0x01095203), tag_num=0x21)
155: 0x0726 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s067" with entities [EventEntity, EventEntity], work=[24*, 0*]
156: 0x0737 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
157: 0x0748 [0x1C] WAIT(100* ticks)
158: 0x074B [0x2B] Dauperiat (ID: 17388033/0x01095201) [7957*]:
    → "The count realized that Atarefaunet would eventually be executed under San d'Orian law, but the condemned man needed to be taken care of before any inquisitions into his crimes had begun."
159: 0x0752 [0x23] WAIT_FOR_DIALOG_INTERACTION
160: 0x0753 [0x52] END_LOAD_SCHEDULER: End scheduler "s067" with entities [EventEntity, EventEntity], work=24*
161: 0x0762 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
162: 0x0773 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s068" with entities [EventEntity, EventEntity], work=[24*, 0*]
163: 0x0784 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7958*]:
    → "And so, he bought off the oubliette guard and arranged for poison to be mixed with Atarefaunet's meal."
164: 0x078B [0x23] WAIT_FOR_DIALOG_INTERACTION
165: 0x078C [0x2B] Dauperiat (ID: 17388033/0x01095201) [7959*]:
    → "But this was exactly what Atarefaunet was waiting for. Feigning death by poison was by far the preferable option to hanging or decapitation!"
166: 0x0793 [0x23] WAIT_FOR_DIALOG_INTERACTION
167: 0x0794 [0x52] END_LOAD_SCHEDULER: End scheduler "s068" with entities [EventEntity, EventEntity], work=24*
168: 0x07A3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
169: 0x07B4 [0x1C] WAIT(60* ticks)
170: 0x07B7 [0x35] LOAD_ZONE_NO_CLOSE(zone_id=149*)
171: 0x07BA [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()
172: 0x07BB [0x1C] WAIT(90* ticks)
173: 0x07BE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x23)
174: 0x07C5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x15)
175: 0x07CC [0x5D] SET_MUSIC_VOLUME(volume=127*, fade_time=120*)
176: 0x07D1 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
177: 0x07D7 [0x4E] SET_ENTITY_HIDE_FLAG: Show Dauperiat (ID: 17388033/0x01095201)
178: 0x07DD [0x80] LOAD_WAIT(entity=LocalPlayer)
179: 0x07E2 [0x80] LOAD_WAIT(entity=Dauperiat (ID: 17388033/0x01095201))
180: 0x07E7 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Atarefaunet (ID: 17388034/0x01095202)
181: 0x07ED [0x4E] SET_ENTITY_HIDE_FLAG: Hide Monban01 (ID: 17388035/0x01095203)
182: 0x07F3 [0x4A] LocalPlayer looks at Dauperiat (ID: 17388033/0x01095201)
183: 0x07FC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
184: 0x07FD [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
185: 0x0802 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x081E
186: 0x080A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s063" with entities [EventEntity, EventEntity], work=[24*, 0*]
187: 0x081B [0x01] GOTO 0x084B
188: 0x081E [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x083A
189: 0x0826 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s063" with entities [EventEntity, EventEntity], work=[24*, 0*]
190: 0x0837 [0x01] GOTO 0x084B
191: 0x083A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s055" with entities [EventEntity, EventEntity], work=[24*, 0*]

SUBROUTINE_084B:
192: 0x084B [0x27] REQ_SET(priority=0x0B, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x24)
193: 0x0852 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
194: 0x0863 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7960*]:
    → "Heh-heh... Atarefaunet used this opportunity to erase his existence from the world."
195: 0x086A [0x23] WAIT_FOR_DIALOG_INTERACTION
196: 0x086B [0x2B] Dauperiat (ID: 17388033/0x01095201) [7961*]:
    → "And secrets that would cause apoplexy in half a hundred corrupt nobles went with him."
197: 0x0872 [0x23] WAIT_FOR_DIALOG_INTERACTION
198: 0x0873 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Dauperiat (ID: 17388033/0x01095201))
199: 0x0879 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x0893
200: 0x0881 [0x52] END_LOAD_SCHEDULER: End scheduler "s063" with entities [EventEntity, EventEntity], work=24*
201: 0x0890 [0x01] GOTO 0x08BC
202: 0x0893 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x08AD
203: 0x089B [0x52] END_LOAD_SCHEDULER: End scheduler "s063" with entities [EventEntity, EventEntity], work=24*
204: 0x08AA [0x01] GOTO 0x08BC
205: 0x08AD [0x52] END_LOAD_SCHEDULER: End scheduler "s055" with entities [EventEntity, EventEntity], work=24*

SUBROUTINE_08BC:
206: 0x08BC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s056" with entities [EventEntity, EventEntity], work=[24*, 0*]
207: 0x08CD [0x4A] Dauperiat (ID: 17388033/0x01095201) looks at LocalPlayer
208: 0x08D6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
209: 0x08D7 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dauperiat (ID: 17388033/0x01095201) Render.Flags0 and Render.Flags3 conditions are met
210: 0x08DC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x01)
211: 0x08E3 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7962*]:
    → "How you use this knowledge is up to you. But I suggest you avoid doing anything to cross Atarefaunet--not if you're fond of your current breathing state."
212: 0x08EA [0x23] WAIT_FOR_DIALOG_INTERACTION
213: 0x08EB [0x2B] Dauperiat (ID: 17388033/0x01095201) [7963*]:
    → "After his "death," Atarefaunet slipped off to a nation in the west, yet rumor has it he's surfaced in these lands again."
214: 0x08F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
215: 0x08F3 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x02)
216: 0x08FA [0x52] END_LOAD_SCHEDULER: End scheduler "s056" with entities [EventEntity, EventEntity], work=24*
217: 0x0909 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s061" with entities [EventEntity, EventEntity], work=[24*, 0*]
218: 0x091A [0x7B] Dauperiat (ID: 17388033/0x01095201) stops talking
219: 0x091F [0x4B] UPDATE_ENTITY_YAW(entity=Dauperiat (ID: 17388033/0x01095201), yaw=20.2°*)
220: 0x0926 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
221: 0x0927 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dauperiat (ID: 17388033/0x01095201) Render.Flags0 and Render.Flags3 conditions are met
222: 0x092C [0x2B] Dauperiat (ID: 17388033/0x01095201) [7964*]:
    → "I don't know who your employer is, but for a normal townsperson this knowledge would be fatal."
223: 0x0933 [0x23] WAIT_FOR_DIALOG_INTERACTION
224: 0x0934 [0x2B] Dauperiat (ID: 17388033/0x01095201) [7965*]:
    → "Take that as advice from the executioner. Farewell."
225: 0x093B [0x23] WAIT_FOR_DIALOG_INTERACTION
226: 0x093C [0x52] END_LOAD_SCHEDULER: End scheduler "s061" with entities [EventEntity, EventEntity], work=24*
227: 0x094B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
228: 0x095C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s062" with entities [EventEntity, EventEntity], work=[24*, 0*]
229: 0x096D [0x27] REQ_SET(priority=0x0B, entity_id=Dauperiat (ID: 17388033/0x01095201), tag_num=0x25)
230: 0x0974 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=120*)
231: 0x0979 [0x1C] WAIT(90* ticks)
232: 0x097C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
233: 0x098D [0x1C] WAIT(120* ticks)
234: 0x0990 [0x2A] GET_REQ_LEVEL(level=11, entity_id=Dauperiat (ID: 17388033/0x01095201))
235: 0x0996 [0x52] END_LOAD_SCHEDULER: End scheduler "s062" with entities [EventEntity, EventEntity], work=24*
236: 0x09A5 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
237: 0x09A9 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
238: 0x09AD [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
239: 0x09B3 [0x80] LOAD_WAIT(entity=LocalPlayer)
240: 0x09B8 [0x46] CAMERA_CONTROL: Restore default settings
241: 0x09BA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
242: 0x09CB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
243: 0x09CD [0x21] END_EVENT
244: 0x09CE [0x00] END_REQSTACK()
```
