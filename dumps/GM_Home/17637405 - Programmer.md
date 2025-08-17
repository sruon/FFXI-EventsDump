# 17637405 - Programmer

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 72 bytes          |
| Total Events     | 2                 |
| References Count | 5                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [70](#event-70)       | 0x0001       |     26 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x1D33      |        7475 |
|       3 | 0x1D34      |        7476 |
|       4 | 0x1D35      |        7477 |

## String References

- **7475**: weather_adj$0,weather_noun$0, Waiting for button press message 1: (ind us_item=128){$256}setlocal 1 (def us_item=128){$256}
- **7476**: Waiting for button press message 2:
- **7477**: Waiting for button press message 3: det_scitemwork=1(198:old boots){$6},det_scitemwork=2(197:old pocket watch){$6},det_scitemwork=3(193:bomb incense){$6},det_scitemwork=4(209:Yasin's sword){$6}, art_bitem=1{$1} status_noun=1{$1},status_adj=1{$1}

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

### Event 70

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F C3 00  80 00 00 01 80 1D 02 80   ...............
0010: 23 1D 03 80 23 1D 04 80  23 21 00                 #...#...#!.     
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0xC3] COPY_STRING_TO_ARRAY(array_index=0x8000, string_value=0x00, additional_value=0x8001)
  2: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=7475*)
    → "weather_adj$0,weather_noun$0, Waiting for button press message 1: (ind us_item=128){$256}setlocal 1 (def us_item=128){$256}"
  3: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7476*)
    → "Waiting for button press message 2:"
  5: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7477*)
    → "Waiting for button press message 3: det_scitemwork=1(198:old boots){$6},det_scitemwork=2(197:old pocket watch){$6},det_scitemwork=3(193:bomb incense){$6},det_scitemwork=4(209:Yasin's sword){$6}, art_bitem=1{$1} status_noun=1{$1},status_adj=1{$1}"
  7: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0019 [0x21] END_EVENT
  9: 0x001A [0x00] END_REQSTACK()
```
