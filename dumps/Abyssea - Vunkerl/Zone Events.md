# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Vunkerl (ID: 217) |
| Block Size       | 684 bytes                   |
| Total Events     | 13                          |
| References Count | 21                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65534](#event-65534)      | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     16 |              3 |
| [65535.2](#event-655352)   | 0x0012       |     41 |              5 |
| [2180](#event-2180)        | 0x003B       |    119 |             15 |
| [65535.3](#event-655353)   | 0x00B2       |     35 |              9 |
| [65535.4](#event-655354)   | 0x00D5       |     35 |              9 |
| [65535.5](#event-655355)   | 0x00F8       |     37 |              5 |
| [65535.6](#event-655356)   | 0x011D       |     37 |              5 |
| [65535.7](#event-655357)   | 0x0142       |      7 |              3 |
| [65535.8](#event-655358)   | 0x0149       |      7 |              3 |
| [65535.9](#event-655359)   | 0x0150       |     24 |              4 |
| [65535.10](#event-6553510) | 0x0168       |    172 |             36 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFA9761  |  4294612833 |
|       1 | 0xAADAE     |      699822 |
|       2 | 0xFFFF4B4E  |  4294921038 |
|       3 | 0x0815      |        2069 |
|       4 | 0x0094      |         148 |
|       5 | 0x0000      |           0 |
|       6 | 0x00F0      |         240 |
|       7 | 0x00C8      |         200 |
|       8 | 0x003C      |          60 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0155      |         341 |
|      11 | 0x0028      |          40 |
|      12 | 0x000D      |          13 |
|      13 | 0x0001      |           1 |
|      14 | 0x0005      |           5 |
|      15 | 0x0002      |           2 |
|      16 | 0x000A      |          10 |
|      17 | 0x0009      |           9 |
|      18 | 0x0046      |          70 |
|      19 | 0x008C      |         140 |
|      20 | 0x00D2      |         210 |

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

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       92 01 F0 FF FF 7F  37 00 80 01 80 02 80 03    ......7.......
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  1: 0x0008 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-354.463*, z=699.822*, y=-46.258*, direction=181.8°*
  2: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       BB 04 80 F0 FF FF  7F B0 92 0D 01 6D 61 69    ...........mai
0020: 6E 05 80 1C 06 80 45 07  80 F0 FF FF 7F F0 FF FF  n.....E.........
0030: 7F 66 64 6F 31 05 80 1C  08 80 00                 .fdo1......     
```

#### Opcodes

```
  0: 0x0012 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17666736/0x010D92B0)], work=[148*, 0*]
  1: 0x0023 [0x1C] WAIT(240* ticks)
  2: 0x0026 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0037 [0x1C] WAIT(60* ticks)
  4: 0x003A [0x00] END_REQSTACK()
```

### Event 2180

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x003B    |
| Data Size    | 119 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   20 01 42 46 01              .BF.
0040: 45 07 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 05  E..........blon.
0050: 80 45 09 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
0060: 05 80 45 07 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  ..E..........ovl
0070: 31 05 80 45 0A 80 F0 FF  FF 7F F0 FF FF 7F 77 61  1..E..........wa
0080: 72 70 05 80 BB 04 80 F0  FF FF 7F B0 92 0D 01 6D  rp.............m
0090: 61 69 6E 05 80 1C 06 80  45 07 80 F0 FF FF 7F F0  ain.....E.......
00A0: FF FF 7F 66 64 6F 31 05  80 1C 08 80 46 00 20 00  ...fdo1.....F. .
00B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x003B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x003D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x003E [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0040 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0051 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0062 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x0073 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
  7: 0x0084 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17666736/0x010D92B0)], work=[148*, 0*]
  8: 0x0095 [0x1C] WAIT(240* ticks)
  9: 0x0098 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x00A9 [0x1C] WAIT(60* ticks)
 11: 0x00AC [0x46] CAMERA_CONTROL: Restore default settings
 12: 0x00AE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x00B0 [0x21] END_EVENT
 14: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       03 00 00 20 10 03  02 00 22 10 03 01 00 21    ... ...."....!
00C0: 10 03 03 00 23 10 32 0B  80 1F 00 00 00 02 00 01  ....#.2.........
00D0: 00 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x00B2 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[32]
  1: 0x00B7 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[34]
  2: 0x00BC [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[33]
  3: 0x00C1 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[35]
  4: 0x00C6 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x00C9 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x00D1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00D3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                03 00 00  20 10 03 02 00 22 10 03       ... ...."..
00E0: 01 00 21 10 03 03 00 23  10 32 0C 80 1F 00 00 00  ..!....#.2......
00F0: 02 00 01 00 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x00D5 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[32]
  1: 0x00DA [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[34]
  2: 0x00DF [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[33]
  3: 0x00E4 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[35]
  4: 0x00E9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x00EC [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x00F4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00F6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x00F7 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F8   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                          03 04 00 07 7F 1A 80 01          ........
0100: 66 05 00 F8 FF FF 7F F8  FF FF 7F 73 68 61 30 53  f..........sha0S
0110: F8 FF FF 7F F8 FF FF 7F  73 68 61 30 00           ........sha0.   
```

#### Opcodes

```
  0: 0x00F8 [0x03] ExtData[1]->WorkLocal[4] = Entity->Race
  1: 0x00FD [0x1A] CALL_SUBROUTINE(address=0x0180)
  2: 0x0100 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[5]
  3: 0x010F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x011C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011D   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         03 04 00               ...
0120: 07 7F 1A 80 01 66 05 00  F8 FF FF 7F F8 FF FF 7F  .....f..........
0130: 73 68 61 31 53 F8 FF FF  7F F8 FF FF 7F 73 68 61  sha1S........sha
0140: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x011D [0x03] ExtData[1]->WorkLocal[4] = Entity->Race
  1: 0x0122 [0x1A] CALL_SUBROUTINE(address=0x0180)
  2: 0x0125 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[5]
  3: 0x0134 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0142  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       AB 03 AC 01 0D 80  00                         .......       
```

#### Opcodes

```
  0: 0x0142 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0144 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0148 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0149  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                             AC 01 05 80 AB 04 00           .......
```

#### Opcodes

```
  0: 0x0149 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x014D [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x014F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0150   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150: 03 04 00 07 7F 1A 80 01  66 05 00 F8 FF FF 7F F8  ........f.......
0160: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x0150 [0x03] ExtData[1]->WorkLocal[4] = Entity->Race
  1: 0x0155 [0x1A] CALL_SUBROUTINE(address=0x0180)
  2: 0x0158 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[5]
  3: 0x0167 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0168    |
| Data Size    | 172 bytes |
| Instructions | 12        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                          03 04 00 07 7F 1A 80 01          ........
0170: 66 05 00 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 00  f..........tlk1.
0180: 03 05 00 04 00 02 05 00  0E 80 05 95 01 08 05 00  ................
0190: 0D 80 01 9A 01 08 05 00  0F 80 14 05 00 10 80 07  ................
01A0: 05 00 11 80 1B 03 05 00  04 00 02 05 00 0E 80 05  ................
01B0: BA 01 08 05 00 0D 80 01  BF 01 08 05 00 0F 80 14  ................
01C0: 05 00 10 80 07 05 00 12  80 1B 03 05 00 04 00 02  ................
01D0: 05 00 0E 80 05 DF 01 08  05 00 0D 80 01 E4 01 08  ................
01E0: 05 00 0F 80 14 05 00 10  80 07 05 00 13 80 1B 03  ................
01F0: 05 00 04 00 02 05 00 0E  80 05 04 02 08 05 00 0D  ................
0200: 80 01 09 02 08 05 00 0F  80 14 05 00 10 80 07 05  ................
0210: 00 14 80 1B                                       ....            
```

#### Opcodes

```
  0: 0x0168 [0x03] ExtData[1]->WorkLocal[4] = Entity->Race
  1: 0x016D [0x1A] CALL_SUBROUTINE(address=0x0180)
  2: 0x0170 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[5]
  3: 0x017F [0x00] END_REQSTACK()

SUBROUTINE_0180:
  4: 0x0180 [0x03] ExtData[1]->WorkLocal[5] = ExtData[1]->WorkLocal[4]
  5: 0x0185 [0x02] IF !(ExtData[1]->WorkLocal[5] > 5*) GOTO 0x0195
  6: 0x018D [0x08] ExtData[1]->WorkLocal[5] -= 1*
  7: 0x0192 [0x01] GOTO 0x019A
  8: 0x0195 [0x08] ExtData[1]->WorkLocal[5] -= 2*

SUBROUTINE_019A:
  9: 0x019A [0x14] ExtData[1]->WorkLocal[5] *= 10*
 10: 0x019F [0x07] ExtData[1]->WorkLocal[5] += 9*
 11: 0x01A4 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x01A5 [0x03] ExtData[1]->WorkLocal[5] = ExtData[1]->WorkLocal[4]
     0x01AA [0x02] IF !(ExtData[1]->WorkLocal[5] > 5*) GOTO 0x01BA
     0x01B2 [0x08] ExtData[1]->WorkLocal[5] -= 1*
     0x01B7 [0x01] GOTO 0x01BF
     0x01BA [0x08] ExtData[1]->WorkLocal[5] -= 2*
     0x01BF [0x14] ExtData[1]->WorkLocal[5] *= 10*
     0x01C4 [0x07] ExtData[1]->WorkLocal[5] += 70*
     0x01C9 [0x1B] RETURN
     0x01CA [0x03] ExtData[1]->WorkLocal[5] = ExtData[1]->WorkLocal[4]
     0x01CF [0x02] IF !(ExtData[1]->WorkLocal[5] > 5*) GOTO 0x01DF
     0x01D7 [0x08] ExtData[1]->WorkLocal[5] -= 1*
     0x01DC [0x01] GOTO 0x01E4
     0x01DF [0x08] ExtData[1]->WorkLocal[5] -= 2*
     0x01E4 [0x14] ExtData[1]->WorkLocal[5] *= 10*
     0x01E9 [0x07] ExtData[1]->WorkLocal[5] += 140*
     0x01EE [0x1B] RETURN
     0x01EF [0x03] ExtData[1]->WorkLocal[5] = ExtData[1]->WorkLocal[4]
     0x01F4 [0x02] IF !(ExtData[1]->WorkLocal[5] > 5*) GOTO 0x0204
     0x01FC [0x08] ExtData[1]->WorkLocal[5] -= 1*
     0x0201 [0x01] GOTO 0x0209
     0x0204 [0x08] ExtData[1]->WorkLocal[5] -= 2*
     0x0209 [0x14] ExtData[1]->WorkLocal[5] *= 10*
     0x020E [0x07] ExtData[1]->WorkLocal[5] += 210*
     0x0213 [0x1B] RETURN
```
