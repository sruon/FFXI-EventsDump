# 17830110 - Jampiaire

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 332 bytes                 |
| Total Events     | 19                        |
| References Count | 6                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [532](#event-532)        | 0x0001       |     43 |              9 |
| [5032](#event-5032)      | 0x002C       |      7 |              2 |
| [5097](#event-5097)      | 0x0033       |      7 |              2 |
| [5099](#event-5099)      | 0x003A       |      7 |              2 |
| [5102](#event-5102)      | 0x0041       |      7 |              2 |
| [5124](#event-5124)      | 0x0048       |      7 |              2 |
| [5130](#event-5130)      | 0x004F       |      7 |              2 |
| [5202](#event-5202)      | 0x0056       |      7 |              2 |
| [106](#event-106)        | 0x005D       |      7 |              2 |
| [5212](#event-5212)      | 0x0064       |      7 |              2 |
| [5214](#event-5214)      | 0x006B       |      7 |              2 |
| [5217](#event-5217)      | 0x0072       |      7 |              2 |
| [5222](#event-5222)      | 0x0079       |      7 |              2 |
| [5107](#event-5107)      | 0x0080       |     66 |             14 |
| [115](#event-115)        | 0x00C2       |      7 |              2 |
| [120](#event-120)        | 0x00C9       |      7 |              2 |
| [65535.1](#event-655351) | 0x00D0       |      4 |              2 |
| [65535.2](#event-655352) | 0x00D4       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001B      |          27 |
|       1 | 0x28D4      |       10452 |
|       2 | 0x1758      |        5976 |
|       3 | 0x2AED      |       10989 |
|       4 | 0x001E      |          30 |
|       5 | 0x0000      |           0 |

## String References

- **10452**: How does a tranquil moment spent amidst the soothing chirps of small birds and the rhythmic crash of waves upon the shoreline sound? This caf<Player>i can provide you with all that and more, [my good sir/my fair lady].
- **10989**: Might I recommend $0? This creamy beverage goes down so smoothly because I awake at the wee hours of each day to pour heaping portions of my love into it.

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

### Event 532

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 62 30 1D  01 80 23 66 00 80 F8 FF  ...tlb0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  62 31 21 00              ......tlb1!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=27*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10452*)
    → "How does a tranquil moment spent amidst the soothing chirps of small birds and the rhythmic crash of waves upon the shoreline sound? This caf<Player>i can provide you with all that and more, [my good sir/my fair lady]."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=27*
  7: 0x002A [0x21] END_EVENT
  8: 0x002B [0x00] END_REQSTACK()
```

### Event 5032

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      92 01 F8 FF              ....
0030: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x002C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0032 [0x00] END_REQSTACK()
```

### Event 5097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0033  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0033 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 5099

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                92 01 F8 FF FF 7F            ......
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x003A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0040 [0x00] END_REQSTACK()
```

### Event 5102

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0041  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0041 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 5124

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0048 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 5130

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               92                 .
0050: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x004F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 5202

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0056  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0056 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005C [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         92 01 F8               ...
0060: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x005D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0063 [0x00] END_REQSTACK()
```

### Event 5212

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0064 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 5214

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   92 01 F8 FF FF             .....
0070: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x006B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 5217

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0072  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0072 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 5222

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0079  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0079 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 5107

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 66 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 1E F0 FF FF 7F 6F 70 4A  F0 FF FF 7F F8 FF FF 7F  .....opJ........
0090: 6F 76 F0 FF FF 7F 66 00  80 F8 FF FF 7F F8 FF FF  ov....f.........
00A0: 7F 74 6C 62 30 03 02 10  02 80 1D 03 80 23 66 00  .tlb0........#f.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 62 31 1C 04 80  .........tlb1...
00C0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0080 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0085 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0086 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0087 [0x4A] LocalPlayer looks at EventEntity
  4: 0x0090 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0091 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0096 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=27*
  7: 0x00A5 [0x03] Work_Zone[2] = 5976*
  8: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=10989*)
    → "Might I recommend $0? This creamy beverage goes down so smoothly because I awake at the wee hours of each day to pour heaping portions of my love into it."
  9: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00AE [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=27*
 11: 0x00BD [0x1C] WAIT(30* ticks)
 12: 0x00C0 [0x21] END_EVENT
 13: 0x00C1 [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C2  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x00C2 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00C8 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C9  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x00C9 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D0  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 95 05 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00D0 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D4  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             96 00                                     ..          
```

#### Opcodes

```
  0: 0x00D4 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x00D5 [0x00] END_REQSTACK()
```
