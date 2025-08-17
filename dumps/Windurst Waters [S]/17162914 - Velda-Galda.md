# 17162914 - Velda-Galda

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 392 bytes                    |
| Total Events     | 23                           |
| References Count | 17                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |     18 |              4 |
| [65535.3](#event-655353) | 0x0014       |     10 |              2 |
| [65535.4](#event-655354) | 0x001E       |      9 |              3 |
| [65535.5](#event-655355) | 0x0027       |      9 |              3 |
| [65535.6](#event-655356) | 0x0030       |     10 |              2 |
| [65535.7](#event-655357) | 0x003A       |     10 |              2 |
| [178](#event-178)        | 0x0044       |      1 |              1 |
| [179](#event-179)        | 0x0045       |      1 |              1 |
| [65535.8](#event-655358) | 0x0046       |     21 |              5 |
| [65535.9](#event-655359) | 0x005B       |     19 |              5 |
| [177](#event-177)        | 0x006E       |     18 |              6 |
| [180](#event-180)        | 0x0080       |     18 |              6 |
| [181](#event-181)        | 0x0092       |     26 |              8 |
| [184](#event-184)        | 0x00AC       |      1 |              1 |
| [235](#event-235)        | 0x00AD       |      1 |              1 |
| [186](#event-186)        | 0x00AE       |      1 |              1 |
| [187](#event-187)        | 0x00AF       |      1 |              1 |
| [188](#event-188)        | 0x00B0       |     18 |              6 |
| [21](#event-21)          | 0x00C2       |      1 |              1 |
| [24](#event-24)          | 0x00C3       |      1 |              1 |
| [27](#event-27)          | 0x00C4       |     18 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x7998      |       31128 |
|       4 | 0x13CC      |        5068 |
|       5 | 0xFFFF9A71  |  4294941297 |
|       6 | 0x21E33     |      138803 |
|       7 | 0xE91B      |       59675 |
|       8 | 0xFFFFF803  |  4294965251 |
|       9 | 0x0FFD      |        4093 |
|      10 | 0x001E      |          30 |
|      11 | 0x34A9      |       13481 |
|      12 | 0x34AA      |       13482 |
|      13 | 0x34AB      |       13483 |
|      14 | 0x34AC      |       13484 |
|      15 | 0x3435      |       13365 |
|      16 | 0x35AD      |       13741 |

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

### Event 178

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

### Event 179

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

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1F 00  03 80 04 80 05 80 1F 01        ..........
0050: 6F 4A A2 E2 05 01 18 E2  05 01 00                 oJ.........     
```

#### Opcodes

```
  0: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=31.128*, Z=5.068*, Y=-25.999*
  1: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0050 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0051 [0x4A] Velda-Galda (ID: 17162914/0x0105E2A2) looks at Robel-Akbel (ID: 17162776/0x0105E218)
  4: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   1F 00 06 80 07             .....
0060: 80 08 80 1F 01 6F 4B A2  E2 05 01 09 80 00        .....oK.......  
```

#### Opcodes

```
  0: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=138.803*, Z=59.675*, Y=-2.045*
  1: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0065 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0066 [0x4B] UPDATE_ENTITY_YAW(entity=Velda-Galda (ID: 17162914/0x0105E2A2), yaw=22.5°*)
  4: 0x006D [0x00] END_REQSTACK()
```

### Event 177

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            1E F0                ..
0070: FF FF 7F 1C 0A 80 2B F8  FF FF 7F 0B 80 23 21 00  ......+......#!.
```

#### Opcodes

```
  0: 0x006E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0073 [0x1C] WAIT(30* ticks)
  2: 0x0076 [0x2B] EventEntity [13481*]:
    → "What do you want? Sorry, but now isn't a good timey-wime. There are numerous affairs of state that require my undivided expertaru attention."
  3: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x007E [0x21] END_EVENT
  5: 0x007F [0x00] END_REQSTACK()
```

### Event 180

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 1E F0 FF FF 7F 1C 0A 80  2B F8 FF FF 7F 0C 80 23  ........+......#
0090: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0080 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0085 [0x1C] WAIT(30* ticks)
  2: 0x0088 [0x2B] EventEntity [13482*]:
    → "You must be tired aftaru your long journey. Was Bastok's reply as favorable as the one you received from us? I do hope the reinforcements makey-wake it to Jeuno in time..."
  3: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0090 [0x21] END_EVENT
  5: 0x0091 [0x00] END_REQSTACK()
```

### Event 181

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       1E F0 FF FF 7F 1C  0A 80 2B F8 FF FF 7F 0D    ........+.....
00A0: 80 23 2B F8 FF FF 7F 0E  80 23 21 00              .#+......#!.    
```

#### Opcodes

```
  0: 0x0092 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0097 [0x1C] WAIT(30* ticks)
  2: 0x009A [0x2B] EventEntity [13483*]:
    → "I am one of the Patriarch Protectors, sworn defenders of the Federation's supreme governing body."
  3: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00A2 [0x2B] EventEntity [13484*]:
    → "Be it from within the shadows or on the frontline of a raging battle, my order's duty is to ensure that no harmy-warm comes to the Patriarchs."
  5: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00AA [0x21] END_EVENT
  7: 0x00AB [0x00] END_REQSTACK()
```

### Event 184

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00AC [0x00] END_REQSTACK()
```

### Event 235

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         00                     .  
```

#### Opcodes

```
  0: 0x00AD [0x00] END_REQSTACK()
```

### Event 186

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            00                   . 
```

#### Opcodes

```
  0: 0x00AE [0x00] END_REQSTACK()
```

### Event 187

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AF  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               00                 .
```

#### Opcodes

```
  0: 0x00AF [0x00] END_REQSTACK()
```

### Event 188

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 1E F0 FF FF 7F 1C 0A 80  2B F8 FF FF 7F 0F 80 23  ........+......#
00C0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00B0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B5 [0x1C] WAIT(30* ticks)
  2: 0x00B8 [0x2B] EventEntity [13365*]:
    → "Master Lehko is engagey-waged with other pressing matters at the momentaru. You'll have to come back later."
  3: 0x00BF [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00C0 [0x21] END_EVENT
  5: 0x00C1 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       00                                            .             
```

#### Opcodes

```
  0: 0x00C2 [0x00] END_REQSTACK()
```

### Event 24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          00                                          .            
```

#### Opcodes

```
  0: 0x00C3 [0x00] END_REQSTACK()
```

### Event 27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C4   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:             1E F0 FF FF  7F 1C 0A 80 2B F8 FF FF      ........+...
00D0: 7F 10 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x00C4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C9 [0x1C] WAIT(30* ticks)
  2: 0x00CC [0x2B] EventEntity [13741*]:
    → "Hm? On another top-secretaru mission for the Warlock Warlord, are we? Something about a magic-wagic stone?"
  3: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00D4 [0x21] END_EVENT
  5: 0x00D5 [0x00] END_REQSTACK()
```
