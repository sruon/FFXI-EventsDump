# 17826126 - Zurko-Bazurko

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 888 bytes                 |
| Total Events     | 20                        |
| References Count | 38                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [209](#event-209)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     15 |              5 |
| [65535.2](#event-655352)   | 0x0011       |     83 |             18 |
| [65535.3](#event-655353)   | 0x0064       |     15 |              5 |
| [65535.4](#event-655354)   | 0x0073       |     33 |              3 |
| [65535.5](#event-655355)   | 0x0094       |     33 |              3 |
| [65535.6](#event-655356)   | 0x00B5       |     33 |              3 |
| [65535.7](#event-655357)   | 0x00D6       |     33 |              3 |
| [65535.8](#event-655358)   | 0x00F7       |     33 |              3 |
| [65535.9](#event-655359)   | 0x0118       |     33 |              3 |
| [65535.10](#event-6553510) | 0x0139       |     33 |              3 |
| [65535.11](#event-6553511) | 0x015A       |     33 |              3 |
| [65535.12](#event-6553512) | 0x017B       |     33 |              3 |
| [65535.13](#event-6553513) | 0x019C       |     33 |              3 |
| [65535.14](#event-6553514) | 0x01BD       |     45 |              5 |
| [65535.15](#event-6553515) | 0x01EA       |     57 |              7 |
| [65535.16](#event-6553516) | 0x0223       |     60 |              8 |
| [65535.17](#event-6553517) | 0x025F       |     16 |              4 |
| [65535.18](#event-6553518) | 0x026F       |     16 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x16F81     |       94081 |
|       2 | 0xFFFEDB85  |  4294892421 |
|       3 | 0xFFFFFD76  |  4294966646 |
|       4 | 0x17BD7     |       97239 |
|       5 | 0xFFFECEF0  |  4294889200 |
|       6 | 0x0028      |          40 |
|       7 | 0x18882     |      100482 |
|       8 | 0xFFFEC385  |  4294886277 |
|       9 | 0x19293     |      103059 |
|      10 | 0xFFFEC857  |  4294887511 |
|      11 | 0x0009      |           9 |
|      12 | 0x0041      |          65 |
|      13 | 0x0050      |          80 |
|      14 | 0x19D86     |      105862 |
|      15 | 0xFFFED856  |  4294891606 |
|      16 | 0x13523     |       79139 |
|      17 | 0xFFFF37A1  |  4294916001 |
|      18 | 0xFFFFFF6C  |  4294967148 |
|      19 | 0x172A1     |       94881 |
|      20 | 0xFFFEDA0E  |  4294892046 |
|      21 | 0x006F      |         111 |
|      22 | 0x00C7      |         199 |
|      23 | 0x00BD      |         189 |
|      24 | 0x001E      |          30 |
|      25 | 0x0053      |          83 |
|      26 | 0x0031      |          49 |
|      27 | 0x005A      |          90 |
|      28 | 0x0022      |          34 |
|      29 | 0x0023      |          35 |
|      30 | 0x00C8      |         200 |
|      31 | 0x0801      |        2049 |
|      32 | 0x00B0      |         176 |
|      33 | 0x000A      |          10 |
|      34 | 0x055D      |        1373 |
|      35 | 0x0096      |         150 |
|      36 | 0x0008      |           8 |
|      37 | 0x0001      |           1 |

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

### Event 209

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
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=94.081*, Z=-74.875*, Y=-0.650*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 83 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 00 80 1F 00 04 80  05 80 03 80 1F 01 32 06   2............2.
0020: 80 1F 00 07 80 08 80 03  80 1F 01 1F 00 09 80 0A  ................
0030: 80 03 80 1F 01 AD 02 0B  80 F8 FF FF 7F F8 FF FF  ................
0040: 7F 1C 0C 80 32 0D 80 1F  00 0E 80 0F 80 03 80 1F  ....2...........
0050: 01 1F 00 10 80 11 80 12  80 1F 01 22 01 2F 01 F8  ..........."./..
0060: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=97.239*, Z=-78.096*, Y=-0.650*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  4: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=100.482*, Z=-81.019*, Y=-0.650*
  5: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x002B [0x1F] MOVE_ENTITY: EventEntity moves to X=103.059*, Z=-79.785*, Y=-0.650*
  7: 0x0033 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0035 [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 2 with entities [EventEntity, EventEntity], work=9*
  9: 0x0041 [0x1C] WAIT(65* ticks)
 10: 0x0044 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
 11: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=105.862*, Z=-75.690*, Y=-0.650*
 12: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=79.139*, Z=-51.295*, Y=-0.148*
 14: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 15: 0x005B [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 16: 0x005D [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
 17: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             32 00 80 1F  00 13 80 14 80 03 80 1F      2...........
0070: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0064 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=94.881*, Z=-75.250*, Y=-0.650*
  2: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          5F 06 15 80 F8  FF FF 7F F8 FF FF 7F 70     _...........p
0080: 61 73 30 16 80 5F 07 F8  FF FF 7F F8 FF FF 7F 70  as0.._.........p
0090: 61 73 30 00                                       as0.            
```

#### Opcodes

```
  0: 0x0073 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=111*, entity1=EventEntity, entity2=EventEntity, string="pas0", extra=199*)
  1: 0x0085 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             5F 06 17 80  F8 FF FF 7F F8 FF FF 7F      _...........
00A0: 6C 6B 30 30 18 80 5F 07  F8 FF FF 7F F8 FF FF 7F  lk00.._.........
00B0: 6C 6B 30 30 00                                    lk00.           
```

#### Opcodes

```
  0: 0x0094 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=189*, entity1=EventEntity, entity2=EventEntity, string="lk00", extra=30*)
  1: 0x00A6 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                5F 06 17  80 F8 FF FF 7F F8 FF FF       _..........
00C0: 7F 74 6C 6B 30 19 80 5F  07 F8 FF FF 7F F8 FF FF  .tlk0.._........
00D0: 7F 74 6C 6B 30 00                                 .tlk0.          
```

#### Opcodes

```
  0: 0x00B5 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=189*, entity1=EventEntity, entity2=EventEntity, string="tlk0", extra=83*)
  1: 0x00C7 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   5F 06  17 80 F8 FF FF 7F F8 FF        _.........
00E0: FF 7F 74 6C 6B 31 19 80  5F 07 F8 FF FF 7F F8 FF  ..tlk1.._.......
00F0: FF 7F 74 6C 6B 31 00                              ..tlk1.         
```

#### Opcodes

```
  0: 0x00D6 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=189*, entity1=EventEntity, entity2=EventEntity, string="tlk1", extra=83*)
  1: 0x00E8 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F7   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      5F  06 1A 80 F8 FF FF 7F F8         _........
0100: FF FF 7F 74 6C 6B 30 1B  80 5F 07 F8 FF FF 7F F8  ...tlk0.._......
0110: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x00F7 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=49*, entity1=EventEntity, entity2=EventEntity, string="tlk0", extra=90*)
  1: 0x0109 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0117 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0118   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          5F 06 1A 80 F8 FF FF 7F          _.......
0120: F8 FF FF 7F 74 6C 6B 31  1B 80 5F 07 F8 FF FF 7F  ....tlk1.._.....
0130: F8 FF FF 7F 74 6C 6B 31  00                       ....tlk1.       
```

#### Opcodes

```
  0: 0x0118 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=49*, entity1=EventEntity, entity2=EventEntity, string="tlk1", extra=90*)
  1: 0x012A [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0138 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0139   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             5F 06 1A 80 F8 FF FF           _......
0140: 7F F8 FF FF 7F 74 68 6B  31 1B 80 5F 07 F8 FF FF  .....thk1.._....
0150: 7F F8 FF FF 7F 74 68 6B  31 00                    .....thk1.      
```

#### Opcodes

```
  0: 0x0139 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=49*, entity1=EventEntity, entity2=EventEntity, string="thk1", extra=90*)
  1: 0x014B [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0159 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015A   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                5F 06 1A 80 F8 FF            _.....
0160: FF 7F F8 FF FF 7F 74 68  6B 32 1B 80 5F 07 F8 FF  ......thk2.._...
0170: FF 7F F8 FF FF 7F 74 68  6B 32 00                 ......thk2.     
```

#### Opcodes

```
  0: 0x015A [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=49*, entity1=EventEntity, entity2=EventEntity, string="thk2", extra=90*)
  1: 0x016C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x017A [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017B   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                   5F 06 1C 80 F8             _....
0180: FF FF 7F F8 FF FF 7F 74  6C 62 30 1B 80 5F 07 F8  .......tlb0.._..
0190: FF FF 7F F8 FF FF 7F 74  6C 62 30 00              .......tlb0.    
```

#### Opcodes

```
  0: 0x017B [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=34*, entity1=EventEntity, entity2=EventEntity, string="tlb0", extra=90*)
  1: 0x018D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x019B [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019C   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                      5F 06 1C 80              _...
01A0: F8 FF FF 7F F8 FF FF 7F  74 6C 62 31 1B 80 5F 07  ........tlb1.._.
01B0: F8 FF FF 7F F8 FF FF 7F  74 6C 62 31 00           ........tlb1.   
```

#### Opcodes

```
  0: 0x019C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=34*, entity1=EventEntity, entity2=EventEntity, string="tlb1", extra=90*)
  1: 0x01AE [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x01BC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BD   |
| Data Size    | 45 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                         81 00 F8               ...
01C0: FF FF 7F 5F 06 1D 80 F8  FF FF 7F F8 FF FF 7F 6D  ..._...........m
01D0: 6F 6E 30 1E 80 5F 07 F8  FF FF 7F F8 FF FF 7F 6D  on0.._.........m
01E0: 6F 6E 30 81 01 F8 FF FF  7F 00                    on0.......      
```

#### Opcodes

```
  0: 0x01BD [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x01C3 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=35*, entity1=EventEntity, entity2=EventEntity, string="mon0", extra=200*)
  2: 0x01D5 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  3: 0x01E3 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  4: 0x01E9 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01EA   |
| Data Size    | 57 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                                81 00 F8 FF FF 7F            ......
01F0: 7C 00 F8 FF FF 7F 5F 05  1F 80 F8 FF FF 7F F8 FF  |....._.........
0200: FF 7F 79 67 6F 30 20 80  5F 07 F8 FF FF 7F F8 FF  ..ygo0 ._.......
0210: FF 7F 79 67 6F 30 81 01  F8 FF FF 7F 7C 01 F8 FF  ..ygo0......|...
0220: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x01EA [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x01F0 [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x01F6 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x05 - Load ext scheduler with flag (OpCode 0x5B mode 0, flag 1), ref=2049*, entity1=EventEntity, entity2=EventEntity, string="ygo0", extra=176*)
  3: 0x0208 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  4: 0x0216 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  5: 0x021C [0x7C] EventEntity->Render.Flags2 |= 0x01
  6: 0x0222 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0223   |
| Data Size    | 60 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:          81 00 F8 FF FF  7F 7C 00 F8 FF FF 7F 1C     ......|......
0230: 21 80 5F 05 22 80 F8 FF  FF 7F F8 FF FF 7F 67 61  !._.".........ga
0240: 68 32 23 80 5F 07 F8 FF  FF 7F F8 FF FF 7F 67 61  h2#._.........ga
0250: 68 32 81 01 F8 FF FF 7F  7C 01 F8 FF FF 7F 00     h2......|...... 
```

#### Opcodes

```
  0: 0x0223 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0229 [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x022F [0x1C] WAIT(10* ticks)
  3: 0x0232 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x05 - Load ext scheduler with flag (OpCode 0x5B mode 0, flag 1), ref=1373*, entity1=EventEntity, entity2=EventEntity, string="gah2", extra=150*)
  4: 0x0244 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  5: 0x0252 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  6: 0x0258 [0x7C] EventEntity->Render.Flags2 |= 0x01
  7: 0x025E [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x025F   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                                               6E                 n
0260: F8 FF FF 7F 24 80 99 F8  FF FF 7F 1C 23 80 00     ....$.......#.. 
```

#### Opcodes

```
  0: 0x025F [0x6E] EventEntity uses emote 8*
  1: 0x0266 [0x99] Wait for EventEntity animation to complete
  2: 0x026B [0x1C] WAIT(150* ticks)
  3: 0x026E [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x026F   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:                                               6E                 n
0270: F8 FF FF 7F 25 80 99 F8  FF FF 7F 1C 23 80 00     ....%.......#.. 
```

#### Opcodes

```
  0: 0x026F [0x6E] EventEntity uses emote 1*
  1: 0x0276 [0x99] Wait for EventEntity animation to complete
  2: 0x027B [0x1C] WAIT(150* ticks)
  3: 0x027E [0x00] END_REQSTACK()
```
