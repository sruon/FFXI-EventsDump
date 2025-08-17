# 17441099 - Stooge Moogle

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Zvahl Keep (ID: 162) |
| Block Size       | 136 bytes                   |
| Total Events     | 8                           |
| References Count | 5                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |      1 |              1 |
| [101](#event-101)     | 0x0002       |      1 |              1 |
| [102](#event-102)     | 0x0003       |      1 |              1 |
| [103](#event-103)     | 0x0004       |      1 |              1 |
| [104](#event-104)     | 0x0005       |      1 |              1 |
| [105](#event-105)     | 0x0006       |     48 |             10 |
| [106](#event-106)     | 0x0036       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x0080      |         128 |
|       2 | 0x005A      |          90 |
|       3 | 0x002D      |          45 |
|       4 | 0x0000      |           0 |

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

### Event 100

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

### Event 101

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

### Event 102

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

### Event 103

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                00                                      .          
```

#### Opcodes

```
  0: 0x0005 [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 48 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   2F 00  4B 21 0A 01 4A 4B 21 0A        /.K!..JK!.
0010: 01 F0 FF FF 7F 4E 00 4B  21 0A 01 1C 00 80 4A F0  .....N.K!.....J.
0020: FF FF 7F 4B 21 0A 01 6F  70 6C 4B 21 0A 01 01 80  ...K!..oplK!....
0030: 02 80 1C 03 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0006 [0x2F] Stooge Moogle (ID: 17441099/0x010A214B)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x000C [0x4A] Stooge Moogle (ID: 17441099/0x010A214B) looks at LocalPlayer
  2: 0x0015 [0x4E] SET_ENTITY_HIDE_FLAG: Show Stooge Moogle (ID: 17441099/0x010A214B)
  3: 0x001B [0x1C] WAIT(20* ticks)
  4: 0x001E [0x4A] LocalPlayer looks at Stooge Moogle (ID: 17441099/0x010A214B)
  5: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0028 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0029 [0x6C] FADE_ENTITY_COLOR(entity_id=Stooge Moogle (ID: 17441099/0x010A214B), end_alpha=128*, fade_time=90*)
  8: 0x0032 [0x1C] WAIT(45* ticks)
  9: 0x0035 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   6C 4B  21 0A 01 04 80 02 80 1C        lK!.......
0040: 02 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0036 [0x6C] FADE_ENTITY_COLOR(entity_id=Stooge Moogle (ID: 17441099/0x010A214B), end_alpha=0*, fade_time=90*)
  1: 0x003F [0x1C] WAIT(90* ticks)
  2: 0x0042 [0x00] END_REQSTACK()
```
