# 17179384 - Tihl Midurhi

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 472 bytes                         |
| Total Events     | 24                                |
| References Count | 28                                |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [105](#event-105)          | 0x0044       |      1 |              1 |
| [106](#event-106)          | 0x0045       |      1 |              1 |
| [107](#event-107)          | 0x0046       |      1 |              1 |
| [108](#event-108)          | 0x0047       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0048       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0057       |     33 |              7 |
| [113](#event-113)          | 0x0078       |      1 |              1 |
| [109](#event-109)          | 0x0079       |      1 |              1 |
| [110](#event-110)          | 0x007A       |      1 |              1 |
| [65535.10](#event-6553510) | 0x007B       |     14 |              3 |
| [65535.11](#event-6553511) | 0x0089       |     16 |              4 |
| [65535.12](#event-6553512) | 0x0099       |      9 |              3 |
| [65535.13](#event-6553513) | 0x00A2       |     11 |              3 |
| [65535.14](#event-6553514) | 0x00AD       |     11 |              3 |
| [65535.15](#event-6553515) | 0x00B8       |     36 |              4 |
| [65535.16](#event-6553516) | 0x00DC       |     25 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFF97C8B  |  4294540427 |
|       5 | 0x52819     |      337945 |
|       6 | 0x011A      |         282 |
|       7 | 0x000D      |          13 |
|       8 | 0xFFF9731C  |  4294538012 |
|       9 | 0x53BCC     |      342988 |
|      10 | 0x020B      |         523 |
|      11 | 0x0003      |           3 |
|      12 | 0x003B      |          59 |
|      13 | 0x002D      |          45 |
|      14 | 0x0014      |          20 |
|      15 | 0x0B1F      |        2847 |
|      16 | 0x001E      |          30 |
|      17 | 0x53913     |      342291 |
|      18 | 0xFFFD7323  |  4294800163 |
|      19 | 0x40E8      |       16616 |
|      20 | 0x58D87     |      363911 |
|      21 | 0xFFFD7587  |  4294800775 |
|      22 | 0x3EFC      |       16124 |
|      23 | 0x0904      |        2308 |
|      24 | 0x0005      |           5 |
|      25 | 0x230CF     |      143567 |
|      26 | 0xFFFD7948  |  4294801736 |
|      27 | 0x21FE      |        8702 |

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

### Event 65535.1

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   00                                    .         
```

#### Opcodes

```
  0: 0x0046 [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          32 03 80 1F 00 04 80 05          2.......
0050: 80 06 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0048 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=-426.869*, Z=337.945*, Y=0.282*
  2: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0055 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      32  07 80 1F 00 08 80 09 80         2........
0060: 0A 80 1F 01 6F 1C 0B 80  66 0C 80 F8 22 06 01 F8  ....o...f..."...
0070: 22 06 01 74 68 6B 31 00                           "..thk1.        
```

#### Opcodes

```
  0: 0x0057 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=-429.284*, Z=342.988*, Y=0.523*
  2: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0064 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0065 [0x1C] WAIT(3* ticks)
  5: 0x0068 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Tihl Midurhi (ID: 17179384/0x010622F8), Tihl Midurhi (ID: 17179384/0x010622F8)], work=59*
  6: 0x0077 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0078  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          00                               .       
```

#### Opcodes

```
  0: 0x0078 [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0079  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             00                             .      
```

#### Opcodes

```
  0: 0x0079 [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                00                           .     
```

#### Opcodes

```
  0: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 14 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   1C 0D 80 79 00             ...y.
0080: F8 FF FF 7F F0 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x007B [0x1C] WAIT(45* ticks)
  1: 0x007E [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             1C 0E 80 7B F8 FF FF           ...{...
0090: 7F 4B F8 FF FF 7F 0F 80  00                       .K.......       
```

#### Opcodes

```
  0: 0x0089 [0x1C] WAIT(20* ticks)
  1: 0x008C [0x7B] EventEntity stops talking
  2: 0x0091 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=15.6°*)
  3: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0099  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             1C 10 80 7B F8 FF FF           ...{...
00A0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0099 [0x1C] WAIT(30* ticks)
  1: 0x009C [0x7B] EventEntity stops talking
  2: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       1F 00 11 80 12 80  13 80 1F 01 00             ...........   
```

#### Opcodes

```
  0: 0x00A2 [0x1F] MOVE_ENTITY: EventEntity moves to X=342.291*, Z=-167.133*, Y=16.616*
  1: 0x00AA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         1F 00 14               ...
00B0: 80 15 80 16 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=363.911*, Z=-166.521*, Y=16.124*
  1: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00B7 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B8   |
| Data Size    | 36 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          1C 03 80 5B 17 80 F8 FF          ...[....
00C0: FF 7F F8 FF FF 7F 73 62  65 30 C5 18 80 F8 FF FF  ......sbe0......
00D0: 7F F8 FF FF 7F 73 30 30  32 00 80 00              .....s002...    
```

#### Opcodes

```
  0: 0x00B8 [0x1C] WAIT(40* ticks)
  1: 0x00BB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sbe0" with entities [EventEntity, EventEntity], work=2308*
  2: 0x00CA [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80003230 for entities [EventEntity, EventEntity], work=5*, param=12403
  3: 0x00DB [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DC   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      79 00 F8 FF              y...
00E0: FF 7F FF 22 06 01 32 03  80 1F 00 19 80 1A 80 1B  ..."..2.........
00F0: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x00DC [0x79] EventEntity looks at Lehko Habhoka (ID: 17179391/0x010622FF) (Basic look)
  1: 0x00E6 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x00E9 [0x1F] MOVE_ENTITY: EventEntity moves to X=143.567*, Z=-165.560*, Y=8.702*
  3: 0x00F1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00F3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00F4 [0x00] END_REQSTACK()
```
