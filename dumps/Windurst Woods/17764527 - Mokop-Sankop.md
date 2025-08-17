# 17764527 - Mokop-Sankop

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 120 bytes                |
| Total Events     | 7                        |
| References Count | 6                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [50](#event-50)       | 0x0001       |      8 |              5 |
| [51](#event-51)       | 0x0009       |      8 |              5 |
| [60](#event-60)       | 0x0011       |      8 |              5 |
| [61](#event-61)       | 0x0019       |      8 |              5 |
| [70](#event-70)       | 0x0021       |      8 |              5 |
| [71](#event-71)       | 0x0029       |      8 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D8F      |        7567 |
|       1 | 0x1D90      |        7568 |
|       2 | 0x1D99      |        7577 |
|       3 | 0x1D9A      |        7578 |
|       4 | 0x1DA3      |        7587 |
|       5 | 0x1DA4      |        7588 |

## String References

- **7567**: I'm not too fond of the folksy-wolksy in these parts. All important with their noses in the air and their tails a-waving, but cheap as can be. You folk from other countries need to get cracking!
- **7568**: Them Elvaan sure are strong with their pointy ears and pointy swords! San d'Oria's sure to be in the lead for a long while yet!
- **7577**: There's a store that sells really good instruments here! I'm gonna-wanna sneak off there later. Ah! Shh, don't tell my boss...
- **7578**: There's plenty of bards around, but I'm the best flute player in Vana'diel. You don't believe me? Stay awhile and listen.
- **7587**: O\`h, I left you behindt O\`nly to return to you, oh Windurst!t S\`o rich, your glory sends me blind,t L\`o, praise the Star Sibyl, oh Windurst!t
- **7588**: Windurst is the besty!t You can forget about the resty!t The air, so fair, has a different smell!t It improves my tone, can't you tell?t

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

### Event 50

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7567*)
    → "I'm not too fond of the folksy-wolksy in these parts. All important with their noses in the air and their tails a-waving, but cheap as can be. You folk from other countries need to get cracking!"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0007 [0x21] END_EVENT
  4: 0x0008 [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             1D 01 80 23 20 00 21           ...# .!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7568*)
    → "Them Elvaan sure are strong with their pointy ears and pointy swords! San d'Oria's sure to be in the lead for a long while yet!"
  1: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x000F [0x21] END_EVENT
  4: 0x0010 [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1D 02 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7577*)
    → "There's a store that sells really good instruments here! I'm gonna-wanna sneak off there later. Ah! Shh, don't tell my boss..."
  1: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0017 [0x21] END_EVENT
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1D 03 80 23 20 00 21           ...# .!
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=7578*)
    → "There's plenty of bards around, but I'm the best flute player in Vana'diel. You don't believe me? Stay awhile and listen."
  1: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x001D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x001F [0x21] END_EVENT
  4: 0x0020 [0x00] END_REQSTACK()
```

### Event 70

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0021  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1D 04 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=7587*)
    → "O`h, I left you behindt O`nly to return to you, oh Windurst!t S`o rich, your glory sends me blind,t L`o, praise the Star Sibyl, oh Windurst!t"
  1: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0025 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0027 [0x21] END_EVENT
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 71

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1D 05 80 23 20 00 21           ...# .!
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7588*)
    → "Windurst is the besty!t You can forget about the resty!t The air, so fair, has a different smell!t It improves my tone, can't you tell?t"
  1: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x002F [0x21] END_EVENT
  4: 0x0030 [0x00] END_REQSTACK()
```
