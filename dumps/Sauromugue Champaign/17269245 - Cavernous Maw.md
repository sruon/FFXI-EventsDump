# 17269245 - Cavernous Maw

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Sauromugue Champaign (ID: 120) |
| Block Size       | 384 bytes                      |
| Total Events     | 13                             |
| References Count | 12                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [904](#event-904)        | 0x0001       |    218 |             32 |
| [500](#event-500)        | 0x00DB       |      1 |              1 |
| [501](#event-501)        | 0x00DC       |      1 |              1 |
| [65535.1](#event-655351) | 0x00DD       |     10 |              2 |
| [65535.2](#event-655352) | 0x00E7       |     10 |              2 |
| [65535.3](#event-655353) | 0x00F1       |     10 |              2 |
| [65535.4](#event-655354) | 0x00FB       |     10 |              2 |
| [502](#event-502)        | 0x0105       |      1 |              1 |
| [503](#event-503)        | 0x0106       |      1 |              1 |
| [19](#event-19)          | 0x0107       |      1 |              1 |
| [20](#event-20)          | 0x0108       |      1 |              1 |
| [21](#event-21)          | 0x0109       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CBF      |        7359 |
|       1 | 0x038E      |         910 |
|       2 | 0x1CC1      |        7361 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0x0155      |         341 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0080      |         128 |
|      11 | 0x0078      |         120 |

## String References

- **7359**: An unseen force is drawing you towards the maw.
- **7361**: Raise your $3? [Yes./No.]

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

### Event 904

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 218 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 03  02 10 01 80 24 02 80 03    .H..#.....$...
0010: 80 04 80 25 02 00 10 04  80 00 CC 00 43 00 43 01  ...%........C.C.
0020: 42 46 01 03 01 10 03 80  45 05 80 F0 FF FF 7F F0  BF......E.......
0030: FF FF 7F 66 64 6F 31 04  80 1C 06 80 38 07 80 29  ...fdo1.....8..)
0040: 01 F0 FF FF 7F 09 45 08  80 F0 FF FF 7F F0 FF FF  ......E.........
0050: 7F 61 74 31 37 04 80 45  05 80 F0 FF FF 7F F0 FF  .at17..E........
0060: FF 7F 66 64 69 31 04 80  1C 06 80 45 05 80 F0 FF  ..fdi1.....E....
0070: FF 7F F0 FF FF 7F 62 6C  6F 6E 04 80 45 09 80 F0  ......blon..E...
0080: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 04 80 45 05 80  .......blon..E..
0090: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 04 80 45 08  ........ovl1..E.
00A0: 80 F0 FF FF 7F F0 FF FF  7F 77 61 72 70 04 80 29  .........warp..)
00B0: 01 F0 FF FF 7F 0A 45 05  80 F0 FF FF 7F F0 FF FF  ......E.........
00C0: 7F 62 6C 6F 66 04 80 46  00 01 D7 00 02 00 10 03  .blof..F........
00D0: 80 00 D7 00 01 D7 00 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7359*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x03] Work_Zone[2] = 910*
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7361*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CC
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0021 [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0023 [0x03] Work_Zone[1] = 1*
 12: 0x0028 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0039 [0x1C] WAIT(60* ticks)
 14: 0x003C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x003F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 16: 0x0046 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at17" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 17: 0x0057 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0068 [0x1C] WAIT(60* ticks)
 19: 0x006B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x007C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x008D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x009E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 23: 0x00AF [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x0A)
 24: 0x00B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x00C7 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x00C9 [0x01] GOTO 0x00D7
 27: 0x00CC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00D7
 28: 0x00D4 [0x01] GOTO 0x00D7

SUBROUTINE_00D7:
 29: 0x00D7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x00D9 [0x21] END_EVENT
 31: 0x00DA [0x00] END_REQSTACK()
```

### Event 500

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   00                         .    
```

#### Opcodes

```
  0: 0x00DB [0x00] END_REQSTACK()
```

### Event 501

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         6C F8 FF               l..
00E0: FF 7F 0A 80 0B 80 00                              .......         
```

#### Opcodes

```
  0: 0x00DD [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=120*)
  1: 0x00E6 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      6C  F8 FF FF 7F 04 80 06 80         l........
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E7 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    6C F8 FF FF 7F 0A 80  03 80 00                  l.........     
```

#### Opcodes

```
  0: 0x00F1 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x00FA [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   6C F8 FF FF 7F             l....
0100: 04 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x00FB [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0104 [0x00] END_REQSTACK()
```

### Event 502

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0105  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                00                                      .          
```

#### Opcodes

```
  0: 0x0105 [0x00] END_REQSTACK()
```

### Event 503

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0106  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                   00                                    .         
```

#### Opcodes

```
  0: 0x0106 [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0107  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                      00                                  .        
```

#### Opcodes

```
  0: 0x0107 [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0108  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                          00                               .       
```

#### Opcodes

```
  0: 0x0108 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0109  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                             00                             .      
```

#### Opcodes

```
  0: 0x0109 [0x00] END_REQSTACK()
```
