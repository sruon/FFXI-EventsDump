# 17162735 - Ampiro-Mapiro

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 140 bytes                    |
| Total Events     | 6                            |
| References Count | 7                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [423](#event-423)        | 0x0001       |     38 |             10 |
| [153](#event-153)        | 0x0027       |      5 |              2 |
| [65535.1](#event-655351) | 0x002C       |      5 |              2 |
| [225](#event-225)        | 0x0031       |     22 |              6 |
| [32](#event-32)          | 0x0047       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2AE1      |       10977 |
|       2 | 0x2AE2      |       10978 |
|       3 | 0x2AE3      |       10979 |
|       4 | 0x00AA      |         170 |
|       5 | 0x00A7      |         167 |
|       6 | 0x2AF6      |       10998 |

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

### Event 423

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 38 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 2B F8 FF   J...........+..
0010: FF 7F 01 80 23 2B F8 FF  FF 7F 02 80 23 2B F8 FF  ....#+......#+..
0020: FF 7F 03 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x2B] EventEntity [10977*]:
    → "At first, when the birdmen attacked, I was just really scared... I didn't know what to do."
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x2B] EventEntity [10978*]:
    → "But then I realized that I had to fight for my Windurst. So I stayed behind all the grownups and kept casting the cure spell that my teacher taught me on them."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x2B] EventEntity [10979*]:
    → "I was so happy-wappy to see my spells making some of them feel better rightaru away!"
  7: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0025 [0x21] END_EVENT
  9: 0x0026 [0x00] END_REQSTACK()
```

### Event 153

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      B6  00 04 80 00                     .....    
```

#### Opcodes

```
  0: 0x0027 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=170*)
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      B6 00 05 80              ....
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x002C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=167*)
  1: 0x0030 [0x00] END_REQSTACK()
```

### Event 225

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 2B F8 FF   J...........+..
0040: FF 7F 06 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0031 [0x4A] EventEntity looks at LocalPlayer
  1: 0x003A [0x1C] WAIT(30* ticks)
  2: 0x003D [0x2B] EventEntity [10998*]:
    → "Woohoo, class dismissed! We're gonna have so much fun in Heavens Tower--I'm bringing all my toys!"
  3: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0045 [0x21] END_EVENT
  5: 0x0046 [0x00] END_REQSTACK()
```

### Event 32

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
