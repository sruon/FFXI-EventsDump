# 17064127 - Galloping Chocobo

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Chocobo Circuit (ID: 70) |
| Block Size       | 104 bytes                |
| Total Events     | 4                        |
| References Count | 4                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [383](#event-383)     | 0x0001       |     20 |              7 |
| [384](#event-384)     | 0x0015       |     16 |              5 |
| [385](#event-385)     | 0x0025       |     16 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2603      |        9731 |
|       1 | 0x2604      |        9732 |
|       2 | 0x2607      |        9735 |
|       3 | 0x2608      |        9736 |

## String References

- **9731**: What? You wanna know which chocobo's fastest? My MegaFlare, of course!
- **9732**: I've been puttin' my own chocobo raisin' theory to the test in the real world, and so far I'm undefeated in all official races!
- **9735**: Mwahahaha!!! MegaFlare has once again proven my genius!
- **9736**: <Sigh> The higher you climb, the steeper it gets, huh? Looks like its back to the drawin' board for me...

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

### Event 383

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 20 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    79 00 F8 FF FF 7F F0  FF FF 7F 1D 00 80 23 1D   y............#.
0010: 01 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0001 [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=9731*)
    → "What? You wanna know which chocobo's fastest? My MegaFlare, of course!"
  2: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000F [0x1D] PRINT_EVENT_MESSAGE(message_id=9732*)
    → "I've been puttin' my own chocobo raisin' theory to the test in the real world, and so far I'm undefeated in all official races!"
  4: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0013 [0x21] END_EVENT
  6: 0x0014 [0x00] END_REQSTACK()
```

### Event 384

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                79 00 F8  FF FF 7F F0 FF FF 7F 1D       y..........
0020: 02 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0015 [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=9735*)
    → "Mwahahaha!!! MegaFlare has once again proven my genius!"
  2: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0023 [0x21] END_EVENT
  4: 0x0024 [0x00] END_REQSTACK()
```

### Event 385

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                79 00 F8  FF FF 7F F0 FF FF 7F 1D       y..........
0030: 03 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0025 [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=9736*)
    → "<Sigh> The higher you climb, the steeper it gets, huh? Looks like its back to the drawin' board for me..."
  2: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0033 [0x21] END_EVENT
  4: 0x0034 [0x00] END_REQSTACK()
```
