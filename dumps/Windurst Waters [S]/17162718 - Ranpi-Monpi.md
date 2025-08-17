# 17162718 - Ranpi-Monpi

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 92 bytes                     |
| Total Events     | 5                            |
| References Count | 3                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [117](#event-117)     | 0x0001       |      1 |              1 |
| [118](#event-118)     | 0x0002       |      1 |              1 |
| [119](#event-119)     | 0x0003       |     23 |              7 |
| [120](#event-120)     | 0x001A       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2CF1      |       11505 |
|       1 | 0x2CF2      |       11506 |
|       2 | 0x2D06      |       11526 |

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

### Event 117

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

### Event 118

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

### Event 119

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          1E F0 FF FF 7F  2B DE E1 05 01 00 80 23     .....+......#
0010: 2B DE E1 05 01 01 80 23  21 00                    +......#!.      
```

#### Opcodes

```
  0: 0x0003 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0008 [0x2B] Ranpi-Monpi (ID: 17162718/0x0105E1DE) [11505*]:
    → "I truly wish nozing more zan to be able to eat unique and extraordinarily new delectable foods..."
  2: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0010 [0x2B] Ranpi-Monpi (ID: 17162718/0x0105E1DE) [11506*]:
    → "But I fear zere are no such chefs left here een Windurst..."
  4: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0018 [0x21] END_EVENT
  6: 0x0019 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 2B            .....+
0020: DE E1 05 01 02 80 23 21  00                       ......#!.       
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x2B] Ranpi-Monpi (ID: 17162718/0x0105E1DE) [11526*]:
    → "I cannot wait for zee time to come when we can take our time and enjoy cooking again!"
  2: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0027 [0x21] END_EVENT
  4: 0x0028 [0x00] END_REQSTACK()
```
