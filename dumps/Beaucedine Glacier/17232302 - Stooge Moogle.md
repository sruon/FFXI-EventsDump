# 17232302 - Stooge Moogle

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Beaucedine Glacier (ID: 111) |
| Block Size       | 144 bytes                    |
| Total Events     | 7                            |
| References Count | 5                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     60 |             12 |
| [65535.2](#event-655352) | 0x003D       |     13 |              3 |
| [501](#event-501)        | 0x004A       |      1 |              1 |
| [502](#event-502)        | 0x004B       |      1 |              1 |
| [503](#event-503)        | 0x004C       |      1 |              1 |
| [504](#event-504)        | 0x004D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x000A      |          10 |
|       2 | 0x0014      |          20 |
|       3 | 0x0080      |         128 |
|       4 | 0x005A      |          90 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    6C AE F1 06 01 00 80  00 80 1C 01 80 2F 00 AE   l.........../..
0010: F1 06 01 4A AE F1 06 01  F0 FF FF 7F 4E 00 AE F1  ...J........N...
0020: 06 01 1C 02 80 4A F0 FF  FF 7F AE F1 06 01 6F 70  .....J........op
0030: 6C AE F1 06 01 03 80 04  80 1C 04 80 00           l............   
```

#### Opcodes

```
  0: 0x0001 [0x6C] FADE_ENTITY_COLOR(entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), end_alpha=0*, fade_time=0*)
  1: 0x000A [0x1C] WAIT(10* ticks)
  2: 0x000D [0x2F] Stooge Moogle (ID: 17232302/0x0106F1AE)->Render.Flags0 &= ~0x80000 // Bit 19
  3: 0x0013 [0x4A] Stooge Moogle (ID: 17232302/0x0106F1AE) looks at LocalPlayer
  4: 0x001C [0x4E] SET_ENTITY_HIDE_FLAG: Show Stooge Moogle (ID: 17232302/0x0106F1AE)
  5: 0x0022 [0x1C] WAIT(20* ticks)
  6: 0x0025 [0x4A] LocalPlayer looks at Stooge Moogle (ID: 17232302/0x0106F1AE)
  7: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x002F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  9: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), end_alpha=128*, fade_time=90*)
 10: 0x0039 [0x1C] WAIT(90* ticks)
 11: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         6C AE F1               l..
0040: 06 01 00 80 04 80 1C 04  80 00                    ..........      
```

#### Opcodes

```
  0: 0x003D [0x6C] FADE_ENTITY_COLOR(entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), end_alpha=0*, fade_time=90*)
  1: 0x0046 [0x1C] WAIT(90* ticks)
  2: 0x0049 [0x00] END_REQSTACK()
```

### Event 501

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                00                           .     
```

#### Opcodes

```
  0: 0x004A [0x00] END_REQSTACK()
```

### Event 502

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   00                         .    
```

#### Opcodes

```
  0: 0x004B [0x00] END_REQSTACK()
```

### Event 503

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      00                       .   
```

#### Opcodes

```
  0: 0x004C [0x00] END_REQSTACK()
```

### Event 504

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         00                     .  
```

#### Opcodes

```
  0: 0x004D [0x00] END_REQSTACK()
```
