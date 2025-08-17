# 17789020 - Weya Salmacha

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Rabao (ID: 247) |
| Block Size       | 700 bytes       |
| Total Events     | 21              |
| References Count | 24              |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [162](#event-162)          | 0x0001       |      1 |              1 |
| [165](#event-165)          | 0x0002       |      1 |              1 |
| [166](#event-166)          | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     21 |              7 |
| [65535.2](#event-655352)   | 0x0019       |     32 |              8 |
| [65535.3](#event-655353)   | 0x0039       |     21 |              7 |
| [65535.4](#event-655354)   | 0x004E       |     13 |              3 |
| [65535.5](#event-655355)   | 0x005B       |     33 |              3 |
| [65535.6](#event-655356)   | 0x007C       |     33 |              3 |
| [65535.7](#event-655357)   | 0x009D       |     33 |              3 |
| [65535.8](#event-655358)   | 0x00BE       |     33 |              3 |
| [65535.9](#event-655359)   | 0x00DF       |     33 |              3 |
| [65535.10](#event-6553510) | 0x0100       |     33 |              3 |
| [65535.11](#event-6553511) | 0x0121       |     33 |              3 |
| [65535.12](#event-6553512) | 0x0142       |     33 |              3 |
| [65535.13](#event-6553513) | 0x0163       |     33 |              3 |
| [65535.14](#event-6553514) | 0x0184       |     33 |              3 |
| [65535.15](#event-6553515) | 0x01A5       |     33 |              3 |
| [65535.16](#event-6553516) | 0x01C6       |     16 |              3 |
| [65535.17](#event-6553517) | 0x01D6       |     33 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x187D      |        6269 |
|       2 | 0xD799      |       55193 |
|       3 | 0x2726      |       10022 |
|       4 | 0x6492      |       25746 |
|       5 | 0x5A18      |       23064 |
|       6 | 0x1F40      |        8000 |
|       7 | 0x1AF2      |        6898 |
|       8 | 0xFFFF908C  |  4294938764 |
|       9 | 0x1EA0      |        7840 |
|      10 | 0x14A9      |        5289 |
|      11 | 0xDDD8      |       56792 |
|      12 | 0x25C3      |        9667 |
|      13 | 0x001E      |          30 |
|      14 | 0x0035      |          53 |
|      15 | 0x0064      |         100 |
|      16 | 0x0032      |          50 |
|      17 | 0x0008      |           8 |
|      18 | 0x0078      |         120 |
|      19 | 0x0096      |         150 |
|      20 | 0x0034      |          52 |
|      21 | 0x0019      |          25 |
|      22 | 0x0082      |         130 |
|      23 | 0x00C8      |         200 |

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

### Event 162

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

### Event 165

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 166

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 1E 2E 70 0F 01 6F 70  00                       ...p..op.       
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=6.269*, Z=55.193*, Y=10.022*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x1E] EventEntity looks at Irmilant (ID: 17788974/0x010F702E) and starts talking
  4: 0x0016 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0017 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 00 80 1F 00 04 80           2......
0020: 05 80 06 80 1F 01 1F 00  07 80 08 80 09 80 1F 01  ................
0030: 22 01 2F 01 F8 FF FF 7F  00                       "./......       
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=25.746*, Z=23.064*, Y=8.000*
  2: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=6.898*, Z=-28.532*, Y=7.840*
  4: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0030 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x0032 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  7: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 00 80 1F 00 0A 80           2......
0040: 0B 80 0C 80 1F 01 1E F0  FF FF 7F 6F 70 00        ...........op.  
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=5.289*, Z=56.792*, Y=9.667*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x004C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            6B 69                ki
0050: 64 6C 30 F8 FF FF 7F 1C  0D 80 00                 dl0........     
```

#### Opcodes

```
  0: 0x004E [0x6B] STOP_AND_IDLE: EventEntity stops current action and resets to idle (animation="idl0")
  1: 0x0057 [0x1C] WAIT(30* ticks)
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   5F 06 0E 80 F8             _....
0060: FF FF 7F F8 FF FF 7F 74  6C 62 31 0F 80 5F 07 F8  .......tlb1.._..
0070: FF FF 7F F8 FF FF 7F 74  6C 62 31 00              .......tlb1.    
```

#### Opcodes

```
  0: 0x005B [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=53*, entity1=EventEntity, entity2=EventEntity, string="tlb1", extra=100*)
  1: 0x006D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      5F 06 0E 80              _...
0080: F8 FF FF 7F F8 FF FF 7F  74 6C 62 32 0F 80 5F 07  ........tlb2.._.
0090: F8 FF FF 7F F8 FF FF 7F  74 6C 62 32 00           ........tlb2.   
```

#### Opcodes

```
  0: 0x007C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=53*, entity1=EventEntity, entity2=EventEntity, string="tlb2", extra=100*)
  1: 0x008E [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         5F 06 10               _..
00A0: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 0F 80 5F  .........thk1.._
00B0: 07 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 00        .........thk1.  
```

#### Opcodes

```
  0: 0x009D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=50*, entity1=EventEntity, entity2=EventEntity, string="thk1", extra=100*)
  1: 0x00AF [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            5F 06                _.
00C0: 10 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 0F 80  ..........thk2..
00D0: 5F 07 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     _.........thk2. 
```

#### Opcodes

```
  0: 0x00BE [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=50*, entity1=EventEntity, entity2=EventEntity, string="thk2", extra=100*)
  1: 0x00D0 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               5F                 _
00E0: 06 11 80 F8 FF FF 7F F8  FF FF 7F 61 77 77 30 12  ...........aww0.
00F0: 80 5F 07 F8 FF FF 7F F8  FF FF 7F 61 77 77 30 00  ._.........aww0.
```

#### Opcodes

```
  0: 0x00DF [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=8*, entity1=EventEntity, entity2=EventEntity, string="aww0", extra=120*)
  1: 0x00F1 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00FF [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0100   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100: 5F 06 11 80 F8 FF FF 7F  F8 FF FF 7F 61 66 72 30  _...........afr0
0110: 0F 80 5F 07 F8 FF FF 7F  F8 FF FF 7F 61 66 72 30  .._.........afr0
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0100 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=8*, entity1=EventEntity, entity2=EventEntity, string="afr0", extra=100*)
  1: 0x0112 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0120 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0121   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    5F 06 11 80 F8 FF FF  7F F8 FF FF 7F 61 66 72   _...........afr
0130: 31 0F 80 5F 07 F8 FF FF  7F F8 FF FF 7F 61 66 72  1.._.........afr
0140: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0121 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=8*, entity1=EventEntity, entity2=EventEntity, string="afr1", extra=100*)
  1: 0x0133 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0141 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0142   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       5F 06 11 80 F8 FF  FF 7F F8 FF FF 7F 61 6E    _...........an
0150: 67 30 13 80 5F 07 F8 FF  FF 7F F8 FF FF 7F 61 6E  g0.._.........an
0160: 67 30 00                                          g0.             
```

#### Opcodes

```
  0: 0x0142 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=8*, entity1=EventEntity, entity2=EventEntity, string="ang0", extra=150*)
  1: 0x0154 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0162 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0163   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:          5F 06 11 80 F8  FF FF 7F F8 FF FF 7F 75     _...........u
0170: 72 65 30 13 80 5F 07 F8  FF FF 7F F8 FF FF 7F 75  re0.._.........u
0180: 72 65 30 00                                       re0.            
```

#### Opcodes

```
  0: 0x0163 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=8*, entity1=EventEntity, entity2=EventEntity, string="ure0", extra=150*)
  1: 0x0175 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0183 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0184   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:             5F 06 14 80  F8 FF FF 7F F8 FF FF 7F      _...........
0190: 77 61 76 30 13 80 5F 07  F8 FF FF 7F F8 FF FF 7F  wav0.._.........
01A0: 77 61 76 30 00                                    wav0.           
```

#### Opcodes

```
  0: 0x0184 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=52*, entity1=EventEntity, entity2=EventEntity, string="wav0", extra=150*)
  1: 0x0196 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x01A4 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A5   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                5F 06 14  80 F8 FF FF 7F F8 FF FF       _..........
01B0: 7F 70 6F 69 30 12 80 5F  07 F8 FF FF 7F F8 FF FF  .poi0.._........
01C0: 7F 70 6F 69 30 00                                 .poi0.          
```

#### Opcodes

```
  0: 0x01A5 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=52*, entity1=EventEntity, entity2=EventEntity, string="poi0", extra=120*)
  1: 0x01B7 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x01C5 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C6   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                   AD 00  15 80 F8 FF FF 7F F8 FF        ..........
01D0: FF 7F 1C 16 80 00                                 ......          
```

#### Opcodes

```
  0: 0x01C6 [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 0 with entities [EventEntity, EventEntity], work=25*
  1: 0x01D2 [0x1C] WAIT(130* ticks)
  2: 0x01D5 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D6   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                   5F 06  10 80 F8 FF FF 7F F8 FF        _.........
01E0: FF 7F 70 61 73 30 17 80  5F 07 F8 FF FF 7F F8 FF  ..pas0.._.......
01F0: FF 7F 70 61 73 30 00                              ..pas0.         
```

#### Opcodes

```
  0: 0x01D6 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=50*, entity1=EventEntity, entity2=EventEntity, string="pas0", extra=200*)
  1: 0x01E8 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x01F6 [0x00] END_REQSTACK()
```
